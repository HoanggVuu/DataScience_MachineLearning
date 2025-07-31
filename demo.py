import torch
from loguru import logger

logger.debug(torch.cuda.is_available())  # Should print True

# Test if you can actually use the GPU
try:
    x = torch.tensor([1.0, 2.0]).cuda()
    logger.info(f"GPU tensor test successful: {x}")
    logger.debug(f"Current GPU device: {torch.cuda.current_device()}")
except Exception as e:
    logger.error(f"GPU tensor test failed: {e}")