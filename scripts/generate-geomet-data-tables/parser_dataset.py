from markdown_dataset_table import DataDataset


def parse_dataset_layer(code_input):
    dic_dataset = code_input['forecast_models']
    row_list = []
    model_list = []
    for dataset_name, info in dic_dataset.items():
        model = dataset_name.split('_', 1)[0]

        if model not in model_list:
            dataset = DataDataset()
            dataset.id = model
            dataset.name = _get_dataset_label(dic_dataset[dataset_name])
            dataset.extent = dic_dataset[dataset_name]['extent'].split()
            dataset.number_of_layer = 0

            dataset.model_runs, dataset.forecast_hours, dataset.forecast_hour_interval = \
                _get_dataset_schedule(info)

            model_list.append(model)
            row_list.append(dataset)
    return row_list


def get_forecast_model_name(code_input, mcf):
    dic_dataset = code_input['forecast_models']
    for name, info in dic_dataset.items():
        if info['mcf'] == mcf:
            return name.split('_')[0]


def _get_dataset_schedule(dic_dataset):
    if 'forecast_hours' not in dic_dataset.keys():
        return None, None, None
    else:
        if 'model_runs' in dic_dataset:
            model_runs = dic_dataset['model_runs']
        else:
            model_runs = None
        forecast_hours = dic_dataset['forecast_hours']
        forecast_hour_interval = dic_dataset['forecast_hour_interval']

        return model_runs, forecast_hours, forecast_hour_interval


def _get_dataset_label(dic_dataset):
    result_dic = dict()
    result_dic['fr'] = dic_dataset['label_fr']
    result_dic['en'] = dic_dataset['label_en']
    return result_dic
