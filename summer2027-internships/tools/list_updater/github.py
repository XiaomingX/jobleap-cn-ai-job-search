"""GitHub Actions utility functions.
GitHub Actions 公用函数。
"""

import os
import sys
import uuid
from typing import Any


def set_output(key: str, value: Any) -> None:
    """Set a GitHub Actions output variable.
    设置 GitHub Actions 输出变量。

    Args:
        key: The output variable name. (输出变量名称)
        value: The value to set (will be converted to string). (要设置的值，将被转换为字符串)
    """
    output = os.getenv("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as fh:
            # Use delimiter format for multiline values
            delimiter = f"ghadelimiter_{uuid.uuid4()}"
            # Convert value to string and handle multiline
            value_str = str(value)
            if "\n" in value_str or any(char in value_str for char in ["*", "#", "`", "[", "]"]):
                # Use heredoc format for multiline or special character values
                print(f"{key}<<{delimiter}", file=fh)
                print(value_str, file=fh)
                print(delimiter, file=fh)
            else:
                # Simple format for single-line values
                print(f"{key}={value_str}", file=fh)


def fail(why: str) -> None:
    """Set error message and exit with failure.
    设置错误消息并以失败状态退出。

    Args:
        why: The error message to output. (要输出的错误消息)
    """
    set_output("error_message", why)
    sys.exit(1)
