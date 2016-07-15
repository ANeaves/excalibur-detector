from nose.tools import *
import random

#from excalibur.fem import ExcaliburFemConfig, ExcaliburFem, ExcaliburFemError
from excalibur.fem import ExcaliburFem, ExcaliburFemError


# class TestExcaliburFemConfig:
# 
#     def test_fem_config(self):
# 
#         fem_number = 1
#         fem_address = '192.168.0.100'
#         fem_port = 6969
#         data_address = '10.0.2.1'
#         config = ExcaliburFemConfig(fem_number, str.encode(fem_address),
#                                     fem_port, str.encode(data_address))
#         assert_equal(config.fem_number, fem_number)
#         assert_equal(config.fem_address, str.encode(fem_address))
#         assert_equal(config.fem_port, fem_port)
#         assert_equal(config.data_address, str.encode(data_address))

class TestExcaliburFemError:

    def test_error_value(self):

        value = 'Test error value'
        with assert_raises_regexp(ExcaliburFemError, value):
            raise ExcaliburFemError(value)


# class TestExcaliburMissingApiLibrary:
# 
#     @classmethod
#     def setup_class(cls):
# 
#         cls.fem_id = 1234
#         ExcaliburFem.use_stub_library = False
# 
#     def test_missing_library(self):
# 
#         with assert_raises_regexp(ExcaliburFemError, 'Error loading API library'):
#             fem = ExcaliburFem(self.fem_id)

class TestExcaliburFem:

    @classmethod
    def setup_class(cls):
        cls.fem_id = 1234

        # Enable use of stub library for testing
        ExcaliburFem.use_stub_library = True

        cls.the_fem = ExcaliburFem(cls.fem_id)

    def test_legal_fem_id(self):

        assert_equal(self.fem_id, self.the_fem.get_id())

    def test_illegal_fem_id(self):

        id = -1
        with assert_raises(ExcaliburFemError) as cm:
            bad_fem = ExcaliburFem(id)
        assert_equal(cm.exception.value, 'Error trying to initialise FEM id {}: Illegal ID specified'.format(id))

    def test_fem_id_exception(self):

        temp_fem = ExcaliburFem(1)
        temp_fem.fem_handle = None
        with assert_raises_regexp(
                ExcaliburFemError, 'get_id: resolved FEM object pointer to null'):
            temp_fem.get_id()

    def test_double_close(self):

        the_fem = ExcaliburFem(0)
        the_fem.close()
        with assert_raises(ExcaliburFemError) as cm:
            the_fem.close()
        assert_equal(cm.exception.value, 'close: FEM object pointer has null FEM handle')

    def test_legal_get_ints(self):

        chip_id = 0
        param_id = 1001
        param_len = 10
        (rc, values) = self.the_fem.get_int(chip_id, param_id, param_len)

        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)
        assert_equal(len(values), param_len)
        assert_equal(values, list(range(param_id, param_id+param_len)))

    def test_get_int_exception(self):

        chip_id = 0
        param_id = 1001
        param_len = 10

        temp_fem = ExcaliburFem(1)
        temp_fem.fem_handle = None

        with assert_raises_regexp(
                ExcaliburFemError, 'get_int: resolved FEM object pointer to null'):
            temp_fem.get_int(chip_id, param_id, param_len)

    def test_legal_set_single_int(self):

        chip_id = 0
        param_id = 1001
        value = 1234

        rc = self.the_fem.set_int(chip_id, param_id, value)

        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)

    def test_legal_set_ints(self):

        chip_id = 0
        param_id = 1001
        param_len = 10
        values = list(range(param_id, param_id + param_len))

        rc = self.the_fem.set_int(chip_id, param_id, values)

        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)

    def test_illegal_set_int(self):

        chip_id = 0
        param_id = 10001
        values = [3.14]*10

        with assert_raises(ExcaliburFemError) as cm:
            rc = self.the_fem.set_int(chip_id, param_id, values)
        assert_equal(cm.exception.value, 'set_int: non-integer value specified')

    def test_legal_set_and_get_int(self):

        chip_id = 0
        param_id = 10002
        param_len = 100
        values_in = [random.randint(0, 1000000) for x in range(param_len)]

        rc = self.the_fem.set_int(chip_id, param_id, values_in)
        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)

        (rc, values_out) = self.the_fem.get_int(chip_id, param_id, param_len)
        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)
        assert_equal(values_in, values_out)

    def test_legal_cmd(self):

        chip_id = 0
        cmd_id = 1
        rc = self.the_fem.cmd(chip_id, cmd_id)
        assert_equal(rc, ExcaliburFem.FEM_RTN_OK)

    def test_illegal_cmd(self):

        chip_id  = 0;
        cmd_id = -1
        rc = self.the_fem.cmd(chip_id, cmd_id)
        assert_equal(rc, ExcaliburFem.FEM_RTN_UNKNOWNOPID)

    def test_cmd_exception(self):

        chip_id = 0
        cmd_id = 1

        temp_fem = ExcaliburFem(1)
        temp_fem.fem_handle = None

        with assert_raises_regexp(
                ExcaliburFemError, 'cmd: resolved FEM object pointer to null'):
            temp_fem.cmd(chip_id, cmd_id)
