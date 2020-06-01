"""
 Copyright (C) 2018-2020 Intel Corporation
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import os
import pytest
import sys
import logging as log
from common.samples_common_test_clas import SamplesCommonTestClass
from common.samples_common_test_clas import get_tests
from common.common_utils import parse_avg_err

log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)

test_data_nthreads = get_tests(cmd_params={'i': [os.path.join('ark', 'dev93_10.ark')],
                                           'm': [os.path.join('FP32', 'wsj_dnn5b.xml')],
                                           'bs': [1, 2],
                                           'o': ['res_output.ark'],
                                           'r': [os.path.join('ark', 'dev93_scores_10.ark')],
                                           'qb': [8, 16],
                                           'nthreads': [1],
                                           'd': ['CPU']},
                               use_device=['d']
                               )

test_data_nthreads_negative = get_tests(cmd_params={'i': [os.path.join('ark', 'dev93_10.ark')],
                                                    'm': [os.path.join('FP32', 'wsj_dnn5b.xml')],
                                                    'bs': [1],
                                                    'o': ['res_output.ark'],
                                                    'r': [os.path.join('ark', 'dev93_scores_10.ark')],
                                                    'qb': [8],
                                                    'nthreads': [0, -2],
                                                    'd': ['CPU']},
                                        use_device=['d']
                                        )


class TestSpeechSample(SamplesCommonTestClass):
    @classmethod
    def setup_class(cls):
        cls.sample_name = 'speech_sample'
        cls.threshold = 0.06
        super().setup_class()

    @pytest.mark.parametrize("param", test_data_nthreads)
    def test_speech_sample_nthreads(self, param):
        stdout = self._test(param).split('\n')
        assert os.path.isfile(param['o']), "Ark file after infer was not found"

        avg_error = parse_avg_err(stdout)
        log.info('Average scores diff: {}'.format(avg_error))
        assert avg_error <= self.threshold

    @pytest.mark.parametrize("param", test_data_nthreads_negative)
    def test_speech_sample_nthreads_negative(self, param):
        retcode, stdout, stderr = self._test(param, get_shell_result=True)
        expected_error_msg = "[ ERROR ] Invalid value for 'nthreads' argument"
        assert expected_error_msg in stderr.rstrip(), "Expected error message {}".format(expected_error_msg)
