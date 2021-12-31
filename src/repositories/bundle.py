from sqlalchemy import select
from database.db_manager import dal
from database.models.bundle import Bundle as BundleModel
from dto.bundle import Bundle as BundleDTO
from typing import Optional


class BundleRepository():
    @classmethod
    def get_by_id(cls, bundle_id: int, force_model=False) -> Optional[BundleDTO]:
        with dal.get_session() as session:
            stmt = select(BundleModel).filter_by(bundle_id=bundle_id)
            result = session.execute(stmt)
            first_result = result.first()
            if not first_result:
                return None
            if force_model:
                return first_result[0]
            return BundleRepository.to_dto(first_result[0])

    @classmethod
    def create(cls, bundle: BundleDTO) -> BundleDTO:
        with dal.get_session() as session:
            b = BundleRepository.from_dto(bundle)
            session.add(b)
            session.commit()
            return BundleRepository.to_dto(b)

    @classmethod
    def update(cls, bundle: BundleDTO) -> BundleDTO:
        with dal.get_session() as session:
            b = BundleRepository.from_dto(bundle)
            session.merge(b)
            session.commit()
            return BundleRepository.to_dto(b)

    @classmethod
    def delete(cls, bundle: BundleDTO):
        with dal.get_session() as session:
            b=BundleRepository.from_dto(bundle, fetch=True)
            session.delete(b)
            return session.commit()

    @classmethod
    def to_dto(cls, model: BundleModel) -> BundleDTO:
        return BundleDTO(
            bundle_name=model.bundle_name,
            bundle_id=model.bundle_id,
            amount_spent=model.amount_spent,
            gamekey=model.gamekey,
            uid=model.uid,
            created=model.created,
            total_choices=model.total_choices,
            choices_remaining=model.choices_remaining,
            currency=model.currency,
            is_giftee=model.is_giftee,
            claimed=model.claimed,
            total=model.total,
            path_ids=model.path_ids,
        )

    @classmethod
    def from_dto(cls, bundle: BundleDTO, fetch=False) -> Optional[BundleModel]:
        if bundle.bundle_id and fetch:
            return BundleRepository.get_by_id(bundle.bundle_id, force_model=True)
        else:
            return BundleModel(
                bundle_name=bundle.bundle_name,
                bundle_id=bundle.bundle_id,
                amount_spent=bundle.amount_spent,
                gamekey=bundle.gamekey,
                uid=bundle.uid,
                created=bundle.created,
                total_choices=bundle.total_choices,
                choices_remaining=bundle.choices_remaining,
                currency=bundle.currency,
                is_giftee=bundle.is_giftee,
                claimed=bundle.claimed,
                total=bundle.total,
                path_ids=bundle.path_ids,
            )
