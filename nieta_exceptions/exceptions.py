class BaseError(Exception):
    """基础异常类"""
    def __init__(self, message="", detail=None):
        self.message = message
        self.detail = detail
        super().__init__(self.message)

    def __str__(self):
        if self.detail:
            return f"{self.message}: {self.detail}"
        return self.message

# ---------------------------------------------------------------------------
# 内容审核相关异常
class ContentReviewError(BaseError):
    """通用内容审核失败异常"""
    def __init__(self, message="内容未通过审核", detail=None):
        super().__init__(message, detail)

class TextReviewError(ContentReviewError):
    """文本审核失败异常"""
    def __init__(self, message="文本内容未通过审核", detail=None):
        super().__init__(message, detail)

class ImageReviewError(ContentReviewError):
    """图片审核失败异常"""
    def __init__(self, message="图片内容未通过审核", detail=None):
        super().__init__(message, detail)

class VideoReviewError(ContentReviewError):
    """视频审核失败异常"""
    def __init__(self, message="视频内容未通过审核", detail=None):
        super().__init__(message, detail)

# ---------------------------------------------------------------------------
# 资源处理相关异常
class ResourceError(BaseError):
    """资源处理相关异常基类"""
    pass

class JsonParseError(ResourceError):
    """JSON解析错误异常"""
    def __init__(self, message="JSON解析失败", detail=None):
        super().__init__(message, detail)

class ImageDownloadError(ResourceError):
    """图片下载错误异常"""
    def __init__(self, message="图片下载失败", detail=None):
        super().__init__(message, detail)

class ImageOpenError(ResourceError):
    """图片打开错误异常"""
    def __init__(self, message="图片打开失败", detail=None):
        super().__init__(message, detail)

# ---------------------------------------------------------------------------
# 超时相关异常
class TimeoutError(BaseError):
    """超时相关异常基类"""
    def __init__(self, message="操作超时", detail=None):
        super().__init__(message, detail)

class LLMTimeoutError(TimeoutError):
    """LLM调用超时异常"""
    def __init__(self, message="LLM调用超时", detail=None):
        super().__init__(message, detail)

class MakeImageTimeoutError(TimeoutError):
    """图片生成超时异常"""
    def __init__(self, message="图片生成超时", detail=None):
        super().__init__(message, detail)

class VideoGenerationTimeoutError(TimeoutError):
    """视频生成超时异常"""
    def __init__(self, message="视频生成超时", detail=None):
        super().__init__(message, detail)

class GetHistoryTimeoutError(TimeoutError):
    """获取历史记录超时异常"""
    def __init__(self, message="获取历史记录超时", detail=None):
        super().__init__(message, detail)