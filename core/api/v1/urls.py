from ninja import Router
from .products.handlers import router as product_router


router = Router(tags=['V1'])
router.add_router('/products', product_router)
