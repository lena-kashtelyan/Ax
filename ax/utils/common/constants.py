#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from enum import Enum, unique

# ------------------------- Miscellaneous -------------------------


TS_FMT = "%Y-%m-%d %H:%M:%S.%f"

DEFAULT_WINSORIZATION_LIMITS_MINIMIZATION: tuple[float, float] = (0.0, 0.2)
DEFAULT_WINSORIZATION_LIMITS_MAXIMIZATION: tuple[float, float] = (0.2, 0.0)

TESTENV_ENV_KEY = "TESTENV"
TESTENV_ENV_VAL = "True"


# --------------------------- Warnings ---------------------------


EXPERIMENT_IS_TEST_WARNING = (
    "The is_test flag has been set to True. "
    "This flag is meant purely for development and integration testing purposes. "
    "If you are running a live experiment, please set this flag to False"
)


# ------------------------ Error messages ------------------------


UNEXPECTED_METRIC_COMBINATION = """\
Unexpected combination of dummy base `Metric` class metrics and `Metric` \
subclasses with defined fetching logic.
"""


# ------------------------- Reserved keys -------------------------


@unique
class Keys(str, Enum):
    """Enum of reserved keys in options dicts etc, alphabetized.


    NOTE: Useful for keys in dicts that correspond to kwargs to
    classes or functions and/or are used in multiple places.
    """

    ACQF_KWARGS = "acquisition_function_kwargs"
    AUTOSET_SURROGATE = "autoset_surrogate"
    BATCH_INIT_CONDITIONS = "batch_initial_conditions"
    CANDIDATE_SET = "candidate_set"
    CANDIDATE_SIZE = "candidate_size"
    COST_AWARE_UTILITY = "cost_aware_utility"
    COST_INTERCEPT = "cost_intercept"
    CURRENT_VALUE = "current_value"
    EXPAND = "expand"
    EXPECTED_ACQF_VAL = "expected_acquisition_value"
    EXPERIMENT_TOTAL_CONCURRENT_ARMS = "total_concurrent_arms"
    FIDELITY_FEATURES = "fidelity_features"
    FIDELITY_WEIGHTS = "fidelity_weights"
    FRAC_RANDOM = "frac_random"
    FULL_PARAMETERIZATION = "full_parameterization"
    IMMUTABLE_SEARCH_SPACE_AND_OPT_CONF = "immutable_search_space_and_opt_config"
    LONG_RUN = "long_run"
    MAXIMIZE = "maximize"
    METADATA = "metadata"
    METRIC_NAMES = "metric_names"
    NUM_FANTASIES = "num_fantasies"
    NUM_INNER_RESTARTS = "num_inner_restarts"
    NUM_RESTARTS = "num_restarts"
    NUM_TRACE_OBSERVATIONS = "num_trace_observations"
    OBJECTIVE = "objective"
    ONLY_SURROGATE = "only_surrogate"
    OPTIMIZER_KWARGS = "optimizer_kwargs"
    PAIRWISE_PREFERENCE_QUERY = "pairwise_pref_query"
    PREFERENCE_DATA = "preference_data"
    PRIMARY_SURROGATE = "primary"
    PROJECT = "project"
    QMC = "qmc"
    RAW_INNER_SAMPLES = "raw_inner_samples"
    RAW_SAMPLES = "raw_samples"
    RESUMED_FROM_STORAGE_TS = "resumed_from_storage_timestamps"
    SAMPLER = "sampler"
    SEED_INNER = "seed_inner"
    SEQUENTIAL = "sequential"
    SHORT_RUN = "short_run"
    STATE_DICT = "state_dict"
    STUBBED_METRIC_FULL_SQA = "stubbed_metric_full_sqa"
    SUBCLASS = "subclass"
    SUBSET_MODEL = "subset_model"
    TASK_FEATURES = "task_features"
    TRIAL_COMPLETION_TIMESTAMP = "trial_completion_timestamp"
    WARM_START_REFITTING = "warm_start_refitting"
    X_BASELINE = "X_baseline"
