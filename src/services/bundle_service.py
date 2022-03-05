from dto.bundle import BundleDTO
from dto.raw_order import RawOrderDTO
from typing import List

class BundleService(object):
    def __init__(self, network_service, bundle_repository):
        self.network_service = network_service
        self.bundle_repository = bundle_repository

    def _convert_raw_order_to_bundle(self, raw_order: RawOrderDTO) -> BundleDTO:
        return BundleDTO(
            bundle_name=raw_order.product['human_name'],
            amount_spent=raw_order.amount_spent,
            gamekey=raw_order.gamekey,
            uid=raw_order.uid,
            created=raw_order.created,
            total_choices=raw_order.total_choices,
            choices_remaining=raw_order.choices_remaining,
            currency=raw_order.currency,
            is_giftee=raw_order.is_giftee,
            claimed=raw_order.claimed,
            total=raw_order.total,
            path_ids=raw_order.path_ids
        )

    def retrieve_remote_bundles_with_credentials(self, session: str, csrf: str) -> None:
        raw_orders: List[RawOrderDTO] = self.network_service.fetch_raw_orders(session=session, csrf=csrf)
        [self.bundle_repository.create(self._convert_raw_order_to_bundle(x)) for x in raw_orders]



