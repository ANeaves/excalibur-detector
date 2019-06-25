"""
excalibur_adapter.py - EXCALIBUR adapter for the ODIN server.

Alan Greer
"""
import logging
import re
from tornado.escape import json_decode, json_encode
from odin.adapters.adapter import ApiAdapter, ApiAdapterRequest, ApiAdapterResponse, request_types, response_types, wants_metadata
from odin.adapters.parameter_tree import ParameterTree, ParameterTreeError


class ExcaliburAdapter(ApiAdapter):
    """ExcaliburAdapter class.

    This class provides the adapter interface between the ODIN server and the EXCALIBUR detector
    system, transforming the REST-like API HTTP verbs into the appropriate EXCALIBUR detector
    control actions

    This adapter supports control of all EXCALIBUR adapters to present a 
    clean API for client connections.  The following adapters are controlled
    by this adapter:

    Excalibur control adapter
    Frame Processor adapter
    Frame Receiver adapter
    """

    DEFAULT_CTRL_ADAPTER = 'ctrl'
    DEFAULT_FP_ADAPTER = 'fp'
    DEFAULT_FR_ADAPTER = 'fr'
    CTRL_ADAPTER = 'ctrl_adapter'
    FP_ADAPTER = 'fp_adapter'
    FR_ADAPTER = 'fr_adapter'

    def __init__(self, **kwargs):
        """Initialise the ExcaliburAdapter object.

        :param kwargs: keyword arguments passed to ApiAdapter as options.
        """
        # Initialise the parameter tree
        self._param_tree = None

        # Initialise the empty adapter references
        self._ctrl_adapter = None
        self._fp_adapter = None
        self._fr_adapter = None

        # Setup default adapter names
        self._ctrl_adapter_name = self.DEFAULT_CTRL_ADAPTER
        self._fp_adapter_name = self.DEFAULT_FP_ADAPTER
        self._fr_adapter_name = self.DEFAULT_FR_ADAPTER

        # Override the defaults if any of the adapters have been specified in the config file
        if self.CTRL_ADAPTER in kwargs:
            self._ctrl_adapter_name = kwargs[self.CTRL_ADAPTER]
        if self.FP_ADAPTER in kwargs:
            self._fp_adapter_name = kwargs[self.FP_ADAPTER]
        if self.FR_ADAPTER in kwargs:
            self._fr_adapter_name = kwargs[self.FR_ADAPTER]

        # Initialise the ApiAdapter base class to store adapter options
        super(ExcaliburAdapter, self).__init__(**kwargs)

    def initialize(self, adapters):
        logging.debug("Adapter list: {}".format(adapters))

        # Check for each adapter required to control the Excalibur
        if self._ctrl_adapter_name in adapters:
            self._ctrl_adapter = adapters[self._ctrl_adapter_name]
            logging.info("Excalibur control adapter set to '{}'".format(self._ctrl_adapter_name))
        else:
            logging.error("No ctrl adapter '{}' present in the system".format(self._ctrl_adapter_name))

        if self._fp_adapter_name in adapters:
            self._fp_adapter = adapters[self._fp_adapter_name]
            logging.info("Excalibur fp adapter set to '{}'".format(self._fp_adapter_name))
        else:
            logging.error("No fp adapter '{}' present in the system".format(self._fp_adapter_name))

        if self._fr_adapter_name in adapters:
            self._fr_adapter = adapters[self._fr_adapter_name]
            logging.info("Excalibur fr adapter set to '{}'".format(self._fr_adapter_name))
        else:
            logging.error("No fr adapter '{}' present in the system".format(self._fr_adapter_name))

        # Setup the parameter tree for the adapter
        self._param_tree = ParameterTree({
            'config': {
                'counter_depth': (self.get_counter_depth, self.set_counter_depth, {
                    'allowed_values': ['1', '6', '12', '24']
                })
            }
        })

    @response_types('application/json', default='application/json')
    def get(self, path, request):
        """Handle an HTTP GET request.
        This method handles an HTTP GET request, returning a JSON response.
        :param path: URI path of request
        :param request: HTTP request object
        :return: an ApiAdapterResponse object containing the appropriate response
        """
        try:
            param = path.split('/')[-1]
            response = self._param_tree.get(path, True)[param]
            status_code = 200
        except ParameterTreeError as param_error:
            # Parameter was not present in the parameter tree
            # Forward the get request directly to the control adapter
            return self._ctrl_adapter.get(path, request)

        logging.debug(response)
        content_type = 'application/json'

        return ApiAdapterResponse(response, content_type=content_type, status_code=status_code)

    @response_types('application/json', default='application/json')
    def put(self, path, request):
        """Handle an HTTP PUT request.
        This method handles an HTTP PUT request, returning a JSON response.
        :param path: URI path of request
        :param request: HTTP request object
        :return: an ApiAdapterResponse object containing the appropriate response
        """
        try:
            value = json_decode(request.body)
            if isinstance(value, unicode):
                value = value.encode("utf-8")
            self._param_tree.set(path, value)
            response = {}
            status_code = 200
        except ParameterTreeError as param_error:
            # Parameter was not present in the parameter tree
            # Forward the get request directly to the control adapter
            return self._ctrl_adapter.put(path, request)

        logging.debug(response)
        content_type = 'application/json'

        return ApiAdapterResponse(response, content_type=content_type, status_code=status_code)

    def set_counter_depth(self, value):
        # We need to push the counter depth to both the control adapter
        request = ApiAdapterRequest(json_encode(str(value)))
        self._ctrl_adapter.put('config/counter_depth', request)
        # The bit depth must also be supplied to the fr and fp adapters, with a slightly different format
        request = ApiAdapterRequest(json_encode("{}-bit".format(value)))
        self._fr_adapter.put('config/decoder_config/bitdepth', request)
        self._fp_adapter.put('config/excalibur/bitdepth', request)
        
    def get_counter_depth(self):
        # Request counter depth from control adapter
        request = ApiAdapterRequest(None)
        return self._ctrl_adapter.get('config/counter_depth', request).data['value']
