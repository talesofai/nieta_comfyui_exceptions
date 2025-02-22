# Nieta Exceptions

一个用于处理常见异常情况的Python包。该包提供了一系列预定义的异常类，可以帮助您更好地管理和处理各种错误情况。

## 特性

- 基础异常类 `BaseError`
- 内容审核相关异常
- 资源处理相关异常
- 超时相关异常

## 安装

```bash
pip install nieta-exceptions
```

## 使用示例

```python
from nieta_exceptions import TextReviewError, ImageDownloadError

# 内容审核异常示例
try:
    # 您的代码
    raise TextReviewError("文本包含敏感内容")
except TextReviewError as e:
    print(f"审核失败: {e}")

# 资源处理异常示例
try:
    # 您的代码
    raise ImageDownloadError("无法下载图片", "HTTP 404")
except ImageDownloadError as e:
    print(f"下载失败: {e}")
```

## 异常类型

### 内容审核相关
- ContentReviewError: 通用内容审核失败异常
- TextReviewError: 文本审核失败异常
- ImageReviewError: 图片审核失败异常
- VideoReviewError: 视频审核失败异常

### 资源处理相关
- ResourceError: 资源处理相关异常基类
- JsonParseError: JSON解析错误异常
- ImageDownloadError: 图片下载错误异常
- ImageOpenError: 图片打开错误异常

### 超时相关
- TimeoutError: 超时相关异常基类
- LLMTimeoutError: LLM调用超时异常
- MakeImageTimeoutError: 图片生成超时异常
- VideoGenerationTimeoutError: 视频生成超时异常
- GetHistoryTimeoutError: 获取历史记录超时异常