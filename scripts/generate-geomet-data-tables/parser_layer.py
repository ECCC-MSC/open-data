# function returning a list of row about layers using the geomet yaml
from markdown_layer_table import DataLayer


def parse_layers_yaml(code_input):
    dic_layers = code_input['layers']
    layer_list = []
    for layer_name, data in dic_layers.items():
        if not('phase' in data and data['phase'] == 'beta'):
            if 'layer_definition' not in data:
                layer = DataLayer()
                layer.id = layer_name
                layer.name = _get_layer_label(dic_layers[layer_name])
                layer.webservice = _get_layer_webservice(dic_layers[layer_name])
                layer.styles = _get_layer_style(dic_layers[layer_name])
                layer_list.append(layer)
    return layer_list


def _get_layer_webservice(dic_layer):
    if 'metadata' in dic_layer and 'wcs_enable_request=!*' in dic_layer['metadata']:
        return ['WMS']
    elif dic_layer['type'] == 'raster':
        return ['WMS', 'WCS']
    else:
        return ['WFS', 'WMS']


def _get_layer_label(dic_layer):
    result_dic = dict()
    result_dic['fr'] = dic_layer['label_fr']
    result_dic['en'] = dic_layer['label_en']
    return result_dic


def _get_layer_style(dic_layer):
    if 'styles' in dic_layer:
        result = []
        for style in dic_layer['styles']:
            result.append(style)
        return result
    else:
        return []