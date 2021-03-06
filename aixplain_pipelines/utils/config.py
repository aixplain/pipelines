"""
Copyright 2022 The aiXplain pipeline authors

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

PIPELINES_RUN_URL = os.getenv("PIPELINES_RUN_URL", "https://platform-api.aixplain.com/assets/pipeline/execution/run")
TEST_PIPELINES_RUN_URL = os.getenv("PIPELINES_RUN_URL", "https://dev-platform-api.aixplain.com/assets/pipeline/execution/run")
# GET THE API KEY FROM CMD
TEST_API_KEY = os.getenv("TEST_API_KEY", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")