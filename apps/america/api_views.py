from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType

from .models import America
from apps.korea.models import Korea
from apps.dubai.models import Dubai
from apps.common.models import CarPhoto  # Изменено с .models на apps.common.models

from .serializers import AmericaSerializer
from apps.korea.serializers import KoreaSerializer
from apps.dubai.serializers import DubaiSerializer


class CarsByIdsView(APIView):
    """
    API для получения машин из всех моделей по списку идентификаторов
    Поддерживает GET и POST запросы
    """
    
    def _process_ids(self, ids):
        """Общая логика обработки ids для GET и POST запросов"""
        if not ids:
            return Response(
                {"error": "Параметр 'ids' должен быть непустым списком"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Контекст для сериализаторов
        context = {'request': self.request}
        
        # Предзагрузка связанных объектов
        america_cars = America.objects.filter(id__in=ids).select_related(
            'brand', 'model', 'color', 'manager'
        )
        korea_cars = Korea.objects.filter(id__in=ids).select_related(
            'brand', 'model', 'color', 'manager'
        )
        dubai_cars = Dubai.objects.filter(id__in=ids).select_related(
            'brand', 'model', 'color', 'manager'
        )
        
        # Получаем ContentTypes для всех моделей
        america_ct = ContentType.objects.get_for_model(America)
        korea_ct = ContentType.objects.get_for_model(Korea)
        dubai_ct = ContentType.objects.get_for_model(Dubai)
        
        # Загружаем все фотографии одним запросом
        all_car_ids = list(america_cars.values_list('id', flat=True)) + \
                      list(korea_cars.values_list('id', flat=True)) + \
                      list(dubai_cars.values_list('id', flat=True))
        
        # Получаем все фотографии
        photos = CarPhoto.objects.filter(
            content_type__in=[america_ct, korea_ct, dubai_ct],
            object_id__in=all_car_ids
        )
        
        # Организуем фотографии по модели и ID машины
        photos_map = {}
        for photo in photos:
            key = (photo.content_type_id, photo.object_id)
            if key not in photos_map:
                photos_map[key] = []
            photos_map[key].append(photo)
        
        # Присоединяем фотографии к соответствующим машинам
        for car in america_cars:
            car.prefetched_photos = photos_map.get((america_ct.id, car.id), [])
            
        for car in korea_cars:
            car.prefetched_photos = photos_map.get((korea_ct.id, car.id), [])
            
        for car in dubai_cars:
            car.prefetched_photos = photos_map.get((dubai_ct.id, car.id), [])
        
        # Сериализуем данные
        america_serializer = AmericaSerializer(america_cars, many=True, context=context)
        korea_serializer = KoreaSerializer(korea_cars, many=True, context=context)
        dubai_serializer = DubaiSerializer(dubai_cars, many=True, context=context)
        
        # Добавляем информацию о стране для каждого автомобиля
        america_data = america_serializer.data
        for car in america_data:
            car['country'] = 'America'
        
        korea_data = korea_serializer.data
        for car in korea_data:
            car['country'] = 'Korea'
            
        dubai_data = dubai_serializer.data
        for car in dubai_data:
            car['country'] = 'Dubai'
        
        # Объединяем результаты
        result = {
            'cars': america_data + korea_data + dubai_data
        }
        
        return Response(result)
    
    def get(self, request, format=None):
        """Обработка GET-запроса с параметрами ids в URL"""
        try:
            # Получаем список ID из параметров запроса
            ids_param = request.query_params.get('ids', '')
            
            # Преобразуем строку с ID в список
            if ids_param:
                ids = [int(id_str) for id_str in ids_param.split(',')]
            else:
                ids = []
                
            return self._process_ids(ids)
            
        except ValueError:
            return Response(
                {"error": "Некорректный формат ID. Должны быть целые числа, разделенные запятыми"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request, format=None):
        """Обработка POST-запроса с параметрами ids в теле запроса"""
        try:
            # Получаем список ID из запроса
            ids = request.data.get('ids', [])
            
            if not isinstance(ids, list):
                return Response(
                    {"error": "Параметр 'ids' должен быть списком"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return self._process_ids(ids)
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
