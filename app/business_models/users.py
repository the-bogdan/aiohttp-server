from typing import List, Tuple
from sqlalchemy.orm import selectinload
from sqlalchemy.future import Select, select
from database import User, Base, UserRelation
from utils.custom_exception import ExecutionException
from utils.abstract_business_model import AbstractBusinessModel


class UsersBusinessModel(AbstractBusinessModel):
    async def get(self) -> User:
        user_id = self.request.match_info.get('id')
        user = await self.session.get(User, int(user_id))
        return user

    async def post(self) -> Tuple[List[User], List[Base]]:
        body: dict = await self.request.json()
        filters = body.get('filters', [])
        with_entities = body.get('with_entities', [])
        # TODO Сделать нормлаьную валидацию

        stmt: Select = select(User)
        for filter_ in filters:
            if filter_.get('type', None) in User.__dict__:
                stmt = stmt.filter(getattr(User, filter_['type']) == filter_['value'])

        if 'orders' in with_entities:
            stmt = stmt.options(selectinload('orders'))
        if 'products' in with_entities:
            stmt = stmt.options(selectinload('orders.products'))

        result = await self.session.execute(stmt)
        results: List[User] = [result for result in result.scalars()]

        included = []
        if 'orders' in with_entities:
            for result in results:
                included.extend(result.orders)
        if 'products' in with_entities:
            for result in results:
                for order in result.orders:
                    included.extend(order.products)

        return results, included

    async def put(self) -> User:
        body: dict = await self.request.json()
        attributes = body['data']['attributes']
        # TODO Нормальная валидация
        if 'first_name' not in attributes:
            raise ExecutionException('attributes-error', 'first_name is required')
        if 'last_name' not in attributes:
            raise ExecutionException('attributes-error', 'last_name is required')
        if '_nickname' not in attributes:
            raise ExecutionException('attributes-error', '_nickname is required')
        if '_password' not in attributes:
            raise ExecutionException('attributes-error', '_password is required')

        user = User()
        for attribute, value in attributes.items():
            if attribute in User.__dict__ and attribute != 'id':
                setattr(user, attribute, value)
        self.session.add(user)
        await self.session.commit()
        return user

    async def patch(self) -> User:
        body: dict = await self.request.json()
        attributes = body['data']['attributes']
        # TODO Нормальная валидация

        if 'id' not in attributes:
            raise ExecutionException('attributes-error', 'id is required')

        user = await self.session.get(User, int(attributes['id']))
        if not user:
            raise ExecutionException('entity-error', 'This entity does not exist')

        for attribute, value in attributes.items():
            if attribute in User.__dict__ and attribute != 'id':
                setattr(user, attribute, value)
        self.session.add(user)
        await self.session.commit()
        return user

    async def delete(self) -> User:
        user_id = self.request.match_info.get('id')
        user = await self.session.get(User, int(user_id))
        if user:
            await self.session.delete(user)
        return user

    async def follow(self) -> UserRelation:
        dst_user_id = self.request.match_info.get('id')
        src_user_id = self.request.get('user_id')

        relation = UserRelation(
            dst_user_id=int(dst_user_id),
            src_user_id=int(src_user_id)
        )
        self.session.add(relation)
        await self.session.commit()
        return relation

    async def followers(self) -> List[User]:
        src_user_id = self.request.get('user_id')

        stmt = select(User).join(
            UserRelation, UserRelation.dst_user_id == User.id
        ).filter(
            UserRelation.src_user_id == int(src_user_id)
        )
        followers = await self.session.execute(stmt)
        return followers.scalars()
