# from typing import Tuple, List
# from database import Order, Base
# from sqlalchemy.orm import selectinload
# from sqlalchemy.future import Select, select
# from utils.custom_exception import ExecutionException
# from utils.abstract_business_model import AbstractBusinessModel
#
#
# class OrdersBusinessModel(AbstractBusinessModel):
#     async def get(self) -> Order:
#         order_id = self.request.match_info.get('id')
#         order = await self.session.get(Order, int(order_id))
#         return order
#
#     async def search(self) -> Tuple[List[Order], List[Base]]:
#         body: dict = await self.request.json()
#         filters = body.get('filters', [])
#         with_entities = body.get('with_entities', [])
#         # TODO Нормальная валидация
#
#         stmt: Select = select(Order)
#         for filter_ in filters:
#             if filter_.get('type', None) in Order.__dict__:
#                 stmt = stmt.filter(getattr(Order, filter_['type']) == filter_['value'])
#
#         if 'products' in with_entities:
#             stmt = stmt.options(selectinload('products'))
#         if 'users' in with_entities:
#             stmt = stmt.options(selectinload('user'))
#
#         result = await self.session.execute(stmt)
#         results: List[Order] = [result for result in result.scalars()]
#
#         included = []
#         if 'users' in with_entities:
#             for result in results:
#                 included.append(result.user)
#         if 'products' in with_entities:
#             for result in results:
#                 included.extend(result.products)
#
#         return results, included
#
#     async def create(self) -> Order:
#         body: dict = await self.request.json()
#         attributes = body['data']['attributes']
#         # TODO Нормальная валидация
#
#         if 'number' not in attributes:
#             raise ExecutionException('attributes-error', 'number is required')
#         if 'user_id' not in attributes:
#             raise ExecutionException('attributes-error', 'user_id is required')
#
#         order = Order()
#         for attribute, value in attributes.items():
#             if attribute in Order.__dict__ and attributes != 'id':
#                 setattr(order, attribute, value)
#         self.session.add(order)
#         await self.session.commit()
#         return order
#
#     async def update(self) -> Order:
#         body: dict = await self.request.json()
#         attributes = body['data']['attributes']
#         # TODO Нормальная валидация
#
#         if 'id' not in attributes:
#             raise ExecutionException('attributes-error', 'id is required')
#
#         order = await self.session.get(Order, int(attributes['id']))
#         if not order:
#             raise ExecutionException('entity-error', 'This entity does not exist')
#
#         for attribute, value in attributes.items():
#             if attribute in Order.__dict__ and attribute != 'id':
#                 setattr(order, attribute, value)
#         self.session.add(order)
#         await self.session.commit()
#         return order
#
#     async def delete(self) -> Order:
#         order_id = self.request.match_info.get('id')
#         order = await self.session.get(Order, int(order_id))
#         if order:
#             await self.session.delete(order)
#         return order
#
