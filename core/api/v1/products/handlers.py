from django.http import HttpRequest
from ninja import Router, Query

from core.api.schemas import APIResponse, ListPaginationResponse
from core.api.filters import PaginationIn, PaginationOut
from core.api.v1.products.schemas import ProductSchema
from core.api.v1.products.filters import ProductFilters

from core.apps.products.services.products import BaseProductService, ORMProductService

router = Router(tags=['Products'])

@router.get('',response=APIResponse[ListPaginationResponse[ProductSchema]])
def get_product_list(
    request: HttpRequest,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn]) -> APIResponse[ListPaginationResponse[ProductSchema]]:
    service: BaseProductService = ORMProductService()
    product_list = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count = service.get_product_count()
    pagination_out=PaginationOut(
        total=product_count,
        offset=pagination_in.offset,
        limit=pagination_in.limit,
    )
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    return APIResponse(data=ListPaginationResponse(items=items, pagination=pagination_out ))
