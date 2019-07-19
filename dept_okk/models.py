# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import django_filters
from reference_books.models import partner, cereal_crop, products, Factory


class okk_wheat_quality_control(models.Model):  # входной контроль качества пшеницы
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    Provider   = models.ForeignKey(partner, verbose_name=u'Поставщик')
    CarNumber  = models.CharField(u'Гос.номер автомобиля', max_length=100)
    CerealCrop = models.ForeignKey(cereal_crop, verbose_name=u'Зерновая культура')
    LotWeight  = models.DecimalField(u'Масса партии', max_digits=6, decimal_places=3)

    # Основные параметры зерна
    Grain_Nature         = models.IntegerField(u'Натура', help_text=u'Указывается в грамм/литр')  # масса установленного объема зерна
    Grain_Moisture       = models.IntegerField(u'Влажность', help_text=u'Указывается в %')
    Grain_Vitreous       = models.IntegerField(u'Стекловидность', help_text=u'Указывается в %')
    Grain_Gluten         = models.IntegerField(u'Клейковина', help_text=u'Указывается в %')
    Grain_IDK            = models.IntegerField(u'ИДК', help_text=u'Указывается в усл.ед.')  # индекс деформации клейковины
    Grain_Protein        = models.IntegerField(u'Белок', help_text=u'Указывается в %')

    # Сорная примесь, %
    DustImpurity_OvsyugKukol = models.IntegerField(u'Овсюг/Куколь', help_text=u'Указывается в %') # Овес пустой
    DustImpurity_PolovaSeeds = models.IntegerField(u'Полова/Семена', help_text=u'Указывается в %') # отброс, получающийся при молотьбе хозяйственных растений
    DustImpurity_SprigsSeeds = models.IntegerField(u'Веточки/Семечки', help_text=u'Указывается в %')
    DustImpurity_Fug         = models.IntegerField(u'Сор/Пыль', help_text=u'Указывается в %')
    DustImpurity_Minerals    = models.IntegerField(u'Минеральная примесь', help_text=u'Указывается в %')
    DustImpurity_Spoiled     = models.IntegerField(u'Испорченные', help_text=u'Указывается в %')

    # Зерновая примесь, %
    GrainImpurity_Beaten    = models.DecimalField(u'Битое/Щуплое, %', max_digits=6, decimal_places=2)
    GrainImpurity_Eaten     = models.DecimalField(u'Изъеденное/Зеленое, %', max_digits=6, decimal_places=2)
    GrainImpurity_Rye       = models.DecimalField(u'Рожь/Поврежденное, %', max_digits=6, decimal_places=2)
    GrainImpurity_Barley    = models.DecimalField(u'Ячмень, %', max_digits=6, decimal_places=2)
    GrainImpurity_Sprouted  = models.DecimalField(u'Проросшее, %', max_digits=6, decimal_places=2)

    # Дефекты зерна
    Defect_Small    = models.IntegerField(u'Мелкое', help_text=u'Указывается в %')
    Defect_Soft     = models.IntegerField(u'Мягкая', help_text=u'Указывается в %')
    Defect_Cracks   = models.IntegerField(u'С трещинами', help_text=u'Указывается в %')
    Defect_BlackGerm   = models.IntegerField(u'С черным зародышем', help_text=u'Указывается в %')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='okk_wqc_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='okk_wqc_modifying')

    def __str__(self):
        return u'Партия от ' + self.Date_word.__str__()
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Входной контроль качества пшеницы (ВККП)'
        permissions = (
            ('okk_wqc_list_view', u'ВККП. Просмотр списка'),
            ('okk_wqc_item_view', u'ВККП. Просмотр записи'),
            ('okk_wqc_item_add', u'ВККП. Добавление записи'),
            ('okk_wqc_item_edit', u'ВККП. Редактирование записи'),
        )

# class okkwheatqualitycontrol_filter(django_filters.FilterSet):
#     Date_word = django_filters.DateRangeFilter(label=u'Дата записи')
#
#     class Meta:
#         model = okk_wheat_quality_control
#         fields = ['Provider', 'Date_word']


TYPE_FLOUR_GRADE =  (
    ('supreme', u'Высший сорт'),
    ('second', u'Второй сорт'),
    ('bran', u'Отруби'),
)

class okk_operational_quality_control_flour(models.Model): # оперативный качественный контроль муки на мельнице
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии

    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    FlourGrade  = models.CharField(u'Сорт муки', choices=TYPE_FLOUR_GRADE, max_length=50)
    BatchNumber = models.CharField(u'№ тонны', max_length=50)
    Productivity = models.IntegerField(u'Производительность, кг/час')

    MoistureInfratek = models.DecimalField(u'Влажность/Инфратек, %', max_digits=4, decimal_places=1)
    Residue  = models.DecimalField(u'Остаток, %', max_digits=4, decimal_places=1)
    Foramen  = models.DecimalField(u'Проход, %', max_digits=4, decimal_places=1)
    MetalImpurity  = models.DecimalField(u'Металлопримесь, мг/кг', max_digits=4, decimal_places=1)

    # Вкрапления
    Inclusion_Black = models.CharField(u'Вкрапления черные', max_length=50)
    Inclusion_Brown = models.CharField(u'Вкрапления коричневые', max_length=50)
    Inclusion_Green = models.CharField(u'Вкрапления зеленые', max_length=50)
    Inclusion_Extraneous = models.CharField(u'Посторонние включения', max_length=50)

    # Коэффициенты
    Factor_a = models.CharField(u'Коэффициент a', max_length=50)
    Factor_b = models.CharField(u'Коэффициент b', max_length=50)

    Crunch = models.CharField(u'Хруст (минеральная примесь)', max_length=50)# хруст
    Contamination = models.CharField(u'Зараженность/загрязненность', max_length=50)# зараженность
    AshContent = models.DecimalField(u'Зольность, %', max_digits=5, decimal_places=2)# зольность
    Acidity = models.DecimalField(u'Кислотность, %', max_digits=4, decimal_places=1)# кислотность
    Gluten = models.DecimalField(u'Клейковина отмытая вручную, %', max_digits=4, decimal_places=1)# клейковина отмытая вручную
    IDK = models.DecimalField(u'ИДК, усл.ед.', max_digits=4, decimal_places=1)  # индекс деформации клейковины
    GlutenInfratek = models.IntegerField(u'Клейковина/Инфратек, %')
    Protein = models.DecimalField(u'Белок, %', max_digits=4, decimal_places=1)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='okk_oqcf_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='okk_oqcf_modifying')

    def __str__(self):
        return u'Партия от ' + self.BatchNumber.__str__()
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Оперативный качественный контроль муки на мельнице (ОККММ)'
        permissions = (
            ('okk_oqcf_list_view', u'ОККММ. Просмотр списка'),
            ('okk_oqcf_item_view', u'ОККММ. Просмотр записи'),
            ('okk_oqcf_item_add', u'ОККММ. Добавление записи'),
            ('okk_oqcf_item_edit', u'ОККММ. Редактирование записи'),
        )

class okkoperationalqualitycontrolflour_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = okk_operational_quality_control_flour
        fields = ['Date_word']


class okk_control_grain_moisture(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    # Отлёжка
    Moisture_excuse1 = models.DecimalField(u'Отлёжка 1', max_digits=5, decimal_places=2)
    Moisture_excuse2 = models.DecimalField(u'Отлёжка 2', max_digits=5, decimal_places=2)
    Moisture_excuse3 = models.DecimalField(u'Отлёжка 3', max_digits=5, decimal_places=2)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='okk_cgm_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='okk_cgm_modifying')

    def __str__(self):
        return u'Партия от ' + self.Date_word.__str__()
    class Meta:
        verbose_name = u'Замер '
        verbose_name_plural = u'Контроль увлажнения зерна на мельнице (КУЗМ)'
        permissions = (
            ('okk_cgm_list_view', u'КУЗМ. Просмотр списка'),
            ('okk_cgm_item_view', u'КУЗМ. Просмотр записи'),
            ('okk_cgm_item_add', u'КУЗМ. Добавление записи'),
            ('okk_cgm_item_edit', u'КУЗМ. Редактирование записи'),
        )

class okkcontrolgrainmoisture_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = okk_control_grain_moisture
        fields = ['Date_word']


class okk_operational_quality_control_semolina(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    BatchNumber = models.CharField(u'№ тонны', max_length=50)
    #Productivity = models.IntegerField(u'Производительность', help_text=u'Указывается в кг/час')
    Moisture = models.DecimalField(u'Влажность, %', max_digits=4, decimal_places=1)
    Foramen  = models.DecimalField(u'Проход, %', max_digits=4, decimal_places=1)
    MetalImpurity  = models.DecimalField(u'Металлопримесь, мг/кг', max_digits=5, decimal_places=2)

    # Вкрапления
    Inclusion_Black = models.CharField(u'Вкрапления черные', max_length=50)
    Inclusion_Brown = models.CharField(u'Вкрапления коричневые', max_length=50)
    Inclusion_Green = models.CharField(u'Вкрапления зеленые', max_length=50)
    Inclusion_Extraneous = models.CharField(u'Посторонние включения', max_length=50)

    # Коэффициенты
    Factor_a = models.CharField(u'Коэффициент a', max_length=50)
    Factor_b = models.CharField(u'Коэффициент b', max_length=50)

    Crunch = models.CharField(u'Хруст', max_length=50)# хруст
    Contamination = models.CharField(u'Зараженность', max_length=50)# зараженность
    AshContent = models.IntegerField(u'Зольность', help_text=u'Указывается в %')# зольность

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='okk_oqcs_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='okk_oqcs_modifying')

    def __str__(self):
        return u'Партия от ' + self.Date_word.__str__()
    class Meta:
        verbose_name = u'Замер '
        verbose_name_plural = u'Оперативный контроль качества манной муки (ОККМнМ)'
        permissions = (
            ('okk_oqcs_list_view', u'ОККМнМ. Просмотр списка'),
            ('okk_oqcs_item_view', u'ОККМнМ. Просмотр записи'),
            ('okk_oqcs_item_add', u'ОККМнМ. Добавление записи'),
            ('okk_oqcs_item_edit', u'ОККМнМ. Редактирование записи'),
        )

class okkoperationalqualitycontrolsemolina_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = okk_operational_quality_control_semolina
        fields = ['Date_word']


class okk_packproducts_quality_control(models.Model):  # контроль качества фасованной продукции
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    Product     = models.ForeignKey(products, verbose_name=u'Вид макаронных изделий')
    BatchNumber = models.CharField(u'№ партии', max_length=30)

    # Качественные показатели
    Moisture = models.IntegerField(u'Влажность', help_text=u'Указывается в %')
    DeviationFromAverageLength = models.IntegerField(u'Отклонение от средней длины', help_text=u'Указывается в %')
    Crumb = models.IntegerField(u'Крошка', help_text=u'Указывается в %')
    Deformation = models.IntegerField(u'Деформация', help_text=u'Указывается в %')
    Split = models.IntegerField(u'Раскол', help_text=u'Указывается в %')
    Cut = models.CharField(u'Качество среза', max_length=100)
    ImpregnationTrace = models.CharField(u'Наличие следов непромеса, вкрапления', max_length=100)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='okk_pqc_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='okk_pqc_modifying')

    def __str__(self):
        return u'Партия от ' + self.BatchNumber.__str__()
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Контроль качества фасованной продукции (ККФП)'
        permissions = (
            ('okk_pqc_list_view', u'ККФП. Просмотр списка'),
            ('okk_pqc_item_view', u'ККФП. Просмотр записи'),
            ('okk_pqc_item_add', u'ККФП. Добавление записи'),
            ('okk_pqc_item_edit', u'ККФП. Редактирование записи'),
        )

class okkpackproductsqualitycontrol_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = okk_packproducts_quality_control
        fields = ['Date_word']