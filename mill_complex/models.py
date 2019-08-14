# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import django_filters
from reference_books.models import coworker, magnetic_installations, fixed_assets, BHM, Sil, partner, cereal_crop, tare, Factory

MILL_GANG = (
    ('day_shift', u'Смена дневная'),
    ('night_shift', u'Смена ночная'),
)

# ---------------------------------------------------------------------------------------------------------
# -------------------- Э Л Е В А Т О Р --------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class elevator_grain_intake(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    CarModel        = models.CharField(u'Модель автомобиля', max_length=100)
    CarNumber       = models.CharField(u'Гос.номер автомобиля', max_length=100)
    Provider        = models.ForeignKey(partner, verbose_name=u'Контрагент')

    CerealCrop      = models.ForeignKey(cereal_crop, verbose_name=u'Зерновая культура', blank=True, null=True)
    WeightGross     = models.IntegerField(u'Вес брутто, кг')
    WeightTare      = models.IntegerField(u'Вес тары, кг')
    WeightNet       = models.IntegerField(u'Вес нетто, кг')
    WeightActual    = models.IntegerField(u'Вес фактический, кг')
    WeightCredit    = models.IntegerField(u'Вес зачетный, кг')
    Comment         = models.TextField(u'Комментарий', blank=True, null=True)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_egi_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_egi_modifying')

    def __str__(self):
        return u'Партия от ' + self.Date_word.__str__()
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Учет прихода зерна (УПЗ)'
        permissions = (
            ('m_egi_list_view', u'УПЗ. Просмотр списка'),
            ('m_egi_item_view', u'УПЗ. Просмотр записи'),
            ('m_egi_item_add', u'УПЗ. Добавление записи'),
            ('m_egi_item_edit', u'УПЗ. Редактирование записи'),
        )

class elevatorgrainintake_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = elevator_grain_intake
        fields = []


class elevator_grain_waste_accounting(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    GrainWaste = models.IntegerField(u'Зерноотходы, кг.')
    GrainWasteTopGrade = models.IntegerField(u'Зерноотходы 1 сорта, кг.')
    GrainWasteSecondGrade = models.IntegerField(u'Зерноотходы 2 сорта, кг.')

    Comment = models.TextField(u'Комментарий', blank=True, null=True)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_egwa_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_egwa_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Учёт зерноотходов на элеваторе (ЭУЗО)'
        permissions = (
            ('m_egwa_list_view', u'ЭУЗО. Просмотр списка'),
            ('m_egwa_item_view', u'ЭУЗО. Просмотр записи'),
            ('m_egwa_item_add', u'ЭУЗО. Добавление записи'),
            ('m_egwa_item_edit', u'ЭУЗО. Редактирование записи'),
        )

class elevatorgrainwasteaccounting_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = elevator_grain_waste_accounting
        fields = ['Date_word']


class elevator_shipment_wheat_to_mill(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    Moisture  = models.DecimalField(u'Влажность', max_digits=4, decimal_places=2, help_text=u'Указывается в %')
    Nature    = models.DecimalField(u'Натура', max_digits=6, decimal_places=2, help_text=u'Указывается в грамм/литр')  # масса установленного объема зерна
    Gluten    = models.DecimalField(u'Клейковина', max_digits=4, decimal_places=2, help_text=u'Указывается в %')
    Vitreous  = models.DecimalField(u'Стекловидность', max_digits=4, decimal_places=2, help_text=u'Указывается в %')
    Yellowish = models.DecimalField(u'Желтизна', max_digits=4, decimal_places=2, help_text=u'Указывается в %')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_eswm_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_eswm_modifying')

    def __str__(self):
        return u'Партия от ' + self.Date_word.__str__()
    class Meta:
        verbose_name = u'Партия '
        verbose_name_plural = u'Отгрузка пшеницы на мельницу (ОПМ)'
        permissions = (
            ('m_eswm_list_view', u'ОПМ. Просмотр списка'),
            ('m_eswm_item_view', u'ОПМ. Просмотр записи'),
            ('m_eswm_item_add', u'ОПМ. Добавление записи'),
            ('m_eswm_item_edit', u'ОПМ. Редактирование записи'),
        )

class elevator_shipment_wheat_to_mill_child_sil(models.Model):
    # Показание муки в силосах, в силос
    parent_table = models.ForeignKey(elevator_shipment_wheat_to_mill, on_delete=models.SET_NULL, null=True)
    grain = models.DecimalField(verbose_name=u'кг', max_digits=8, decimal_places=2)
    party = models.DecimalField(verbose_name=u'%', max_digits=4, decimal_places=2)
    sil_num = models.ForeignKey(Sil, verbose_name=u'Силос №', on_delete=models.SET_NULL, null=True)

class elevatorshipmentwheattomill_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = elevator_shipment_wheat_to_mill
        fields = ['Date_word']
# ---------------------------------------------------------------------------------------------------------
# -------------------- М Е Л Ь Н И Ц А --------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
class mill_bagging(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang      = models.CharField(u'Смена', choices=MILL_GANG, max_length=30)

    ReceivedBags_flour = models.IntegerField(u'Получено муки, мешков')
    ReceivedBags_zo = models.IntegerField(u'Получено з/о, мешков')
    ReceivedBags_zelen = models.IntegerField(u'Получено зелен., мешков')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_bag_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_bag_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Учёт мешков'
        permissions = (
            ('m_bag_list_view', u'Учет мешков. Просмотр списка'),
            ('m_bag_item_view', u'Учет мешков. Просмотр записи'),
            ('m_bag_item_add', u'Учет мешков. Добавление записи'),
            ('m_bag_item_edit', u'Учет мешков. Редактирование записи'),
        )

class millbagging_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_bagging
        fields = ['Date_word']


class mill_grain_waste_accounting(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang      = models.CharField(u'Смена', choices=MILL_GANG, max_length=30)

    GrainWaste = models.IntegerField(u'Зерноотходы, кг.')
    Bran = models.IntegerField(u'Отруби, кг.')
    BranSecondGrade = models.IntegerField(u'Отруби 2сорта, кг.')
    Comment = models.TextField(u'Комментарий', blank=True, null=True)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_gwa_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_gwa_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Учёт зерноотходов на мельнице (УЗО)'
        permissions = (
            ('m_gwa_list_view', u'УЗО. Просмотр списка'),
            ('m_gwa_item_view', u'УЗО. Просмотр записи'),
            ('m_gwa_item_add', u'УЗО. Добавление записи'),
            ('m_gwa_item_edit', u'УЗО. Редактирование записи'),
        )

class millgrainwasteaccounting_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_grain_waste_accounting
        fields = ['Date_word']


class mill_control_magnetic_installations(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang      = models.CharField(u'Смена', choices=MILL_GANG, max_length=30)

    CheckPassed = models.ManyToManyField(magnetic_installations,
                                         verbose_name=u'Проверку прошли', related_name='mi_checkpassed',
                                         help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')
    CheckFailed = models.ManyToManyField(magnetic_installations,
                                         verbose_name=u'Проверку не прошли', related_name='mi_checkfailed',
                                         help_text=u'Для указания нескольких исполнителей используйте клавишу Ctrl')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_cmi_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_cmi_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Контроль магнитных установок (КМУ)'
        permissions = (
            ('m_cmi_list_view', u'КМУ. Просмотр списка'),
            ('m_cmi_item_view', u'КМУ. Просмотр записи'),
            ('m_cmi_item_add', u'КМУ. Добавление записи'),
            ('m_cmi_item_edit', u'КМУ. Редактирование записи'),
        )

class millcontrolmagneticinstallations_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_control_magnetic_installations
        fields = ['Date_word']


class mill_laboratory_work(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang      = models.CharField(u'Смена', choices=MILL_GANG, max_length=30)

    # Влажность
    Postponing_One  = models.DecimalField(u'Отлёжка 1', max_digits=4, decimal_places=1)
    Postponing_Two  = models.DecimalField(u'Отлёжка 2', max_digits=4, decimal_places=1)
    Postponing_Three = models.DecimalField(u'Отлёжка 3', max_digits=4, decimal_places=1)
    Grade_Top       = models.DecimalField(u'Высший сорт', max_digits=4, decimal_places=1)
    Grade_Second    = models.DecimalField(u'Второй сорт', max_digits=4, decimal_places=1)

    # Высший сорт
    Remainder_TopGrade = models.DecimalField(u'Остаток в/с', max_digits=4, decimal_places=1)
    Passage_TopGrade = models.DecimalField(u'Проход в/c', max_digits=4, decimal_places=1)
    Yellowish_TopGrade = models.DecimalField(u'Желтизна в/c', max_digits=4, decimal_places=1)
    MetalImpurity_TopGrade = models.DecimalField(u'Металлопримесь в/c', max_digits=4, decimal_places=2)
    Crunch_TopGrade = models.CharField(u'Хруст в/c', max_length=50,
                                       choices=(('not_crunch', u'нет'),('thereis', u'да')))

    # Цвет
    GrainBlack = models.IntegerField(u'Черных')
    GrainBraun = models.IntegerField(u'Коричневых')
    GrainGreen = models.IntegerField(u'Зелёных')
    GrainWhite = models.IntegerField(u'Белых')

    # 2ой сорт
    Remainder_GradeSecond = models.DecimalField(u'Остаток 2ой сорт', max_digits=4, decimal_places=1)
    Passage_GradeSecond = models.DecimalField(u'Проход 2ой сорт', max_digits=4, decimal_places=1)

    Bran_Nature = models.IntegerField(u'Отруби натура, г/л')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_lw_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_lw_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Журнал лабораторных работ (ЖЛр)'
        permissions = (
            ('m_lw_list_view', u'ЖЛр. Просмотр списка'),
            ('m_lw_item_view', u'ЖЛр. Просмотр записи'),
            ('m_lw_item_add', u'ЖЛр. Добавление записи'),
            ('m_lw_item_edit', u'ЖЛр. Редактирование записи'),
        )

class milllaboratorywork_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_laboratory_work
        fields = ['Date_word']


class mill_technological(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')
    Gang      = models.CharField(u'Смена', choices=MILL_GANG, max_length=30)

    # Произведено продукции, кг
    Prod_Semolina           = models.IntegerField(u'Манка')
    Prod_TopGrade_enum      = models.IntegerField(u'Высший сорт счетчик (весы)')
    Prod_SecondGrade_enum   = models.IntegerField(u'2 сорт счетчик (весы)')
    Prod_Bran_enum          = models.IntegerField(u'Отруби счетчик (весы)')
    Prod_GrainWaste         = models.IntegerField(u'Зерноотходы')
    Prod_Bran2Varieties     = models.IntegerField(u'Отруби 2сорта')

    # Выбито в мешки
    KnockedOut_TopGrade_start   = models.IntegerField(u'Высший сорт № поддона от')
    KnockedOut_TopGrade_stop    = models.IntegerField(u'Высший сорт № поддона до')
    KnockedOut_TopGrade         = models.IntegerField(u'Высший сорт, поддонов', blank=True, null=True)
    KnockedOut_SecondGrade      = models.IntegerField(u'2 сорт, поддонов')
    KnockedOut_Semolina         = models.IntegerField(u'Манка, кг.')

    Trans_Workshop              = models.IntegerField(u'Перекачено в цех счетчик, кг')

    Description_work = models.TextField(u'Произведенные работы во время смены')

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_tech_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_tech_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Технологический журнал (ТЖ)'
        permissions = (
            ('m_tech_list_view', u'ТЖ. Просмотр списка'),
            ('m_tech_item_view', u'ТЖ. Просмотр записи'),
            ('m_tech_item_add', u'ТЖ. Добавление записи'),
            ('m_tech_item_edit', u'ТЖ. Редактирование записи'),
        )

class mill_technological_child_bhm(models.Model):
    # Показание муки в БХМ, в %
    parent_table = models.ForeignKey(mill_technological, on_delete=models.SET_NULL, null=True)
    grain = models.IntegerField(verbose_name=u'%')
    bhm_num = models.ForeignKey(BHM, verbose_name=u'БХМ №', on_delete=models.SET_NULL, null=True)

class milltechnological_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_technological
        fields = ['Date_word']


class mill_storage_flour_accounting(models.Model):
    # Фабрика/завод
    Factory = models.ForeignKey(Factory, verbose_name='Организация')

    # Данные о партии
    Date_word = models.DateField(u'Дата контроля')
    Time_word = models.TimeField(u'Время контроля')

    # Мука, кг
    TopGrade            = models.IntegerField(u'Высший сорт, кг')
    SecondGrade         = models.IntegerField(u'Второй сорт, кг')
    TransportTopGrade   = models.IntegerField(u'Муковоз высший сорт, кг')
    TransportSecondGrade = models.IntegerField(u'Муковоз второй сорт, кг')
    Semolina            = models.IntegerField(u'Манка, кг')
    Comment             = models.TextField(u'Комментарий', blank=True, null=True)

    # Контроллер записи
    DateTime_add        = models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    DateTime_update     = models.DateTimeField(u'Дата и время обновления', auto_now=True)
    Create_user         = models.ForeignKey(User, null=True, related_name='m_sfa_creator')
    Update_user         = models.ForeignKey(User, null=True, related_name='m_sfa_modifying')

    def __str__(self):
        return self.Date_word.__str__()+' '+self.Gang
    class Meta:
        verbose_name = u'Смена '
        verbose_name_plural = u'Учет муки на складе (УМС)'
        permissions = (
            ('m_sfa_list_view', u'УМС. Просмотр списка'),
            ('m_sfa_item_view', u'УМС. Просмотр записи'),
            ('m_sfa_item_add', u'УМС. Добавление записи'),
            ('m_sfa_item_edit', u'УМС. Редактирование записи'),
        )

class millstorageflouraccounting_filter(django_filters.FilterSet):
    Date_word = django_filters.DateRangeFilter(label=u'Дата записи')

    class Meta:
        model = mill_storage_flour_accounting
        fields = ['Date_word']