from .models import FinancialYear

years = [(-1, '---Select Financial Year---')]
try:
    date_mapping = map(lambda x: (x[0], x[1]), FinancialYear.objects.values_list('id', 'description'))
    years.extend(list(date_mapping))
except Exception as ex:
    pass


def filter_dates(current):
    all_dict = {x[0]: x[1] for x in FinancialYear.YEARS}
    current_dict = {y[0]: y[1] for y in current}
    not_assigned_lst = list()
    for key, value in all_dict.items():
        if value not in current_dict.values():
            not_assigned_lst.append((key, value))
        continue
    not_assigned_lst.insert(0, (-1, '---Select Financial Year---'))
    return not_assigned_lst
