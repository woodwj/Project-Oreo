import json
import pathlib
import utils
from collections import defaultdict

_basedate_key = 'baseDate'
_dc_key = 'dataCollection|UQL/DataCollection'
_dc_list_key = 'dataList|sequence/object'
_data_id_key = 'dataId'
_mktdata_id_key = 'Market Data'
_data_1d_key = 'item|UQL/Data1d'

_datapoint_list_key = 'dataPointList|sequence/object'
_datapoint_item_key = 'item|UQL/DataPointCurveInstrument'
_dataconv_key = 'dataConvention'
_datatype_key = 'dataType|enum/DataType'
_dlabel1_key = 'label1|variant/string'
_data_value_key = 'dataValue'
_mdldata_key = "object|UQL/ModelData"
_bm_key = "buildMethods|sequence/object"
_datacollection_key = "item|UQL/DataCollection"


#function to read the file name
def read_file(file_name):

    # path lib allows cross platform uniformity
    path = pathlib.Path(file_name)

    # get str of file
    with path.open() as f :
        fileStr = f.read()

    # load file str into dict
    full_dict = json.loads(fileStr)
    full_dict = full_dict[_mdldata_key]

    # data collection - # drop down into next level the list holding each data collection data set
    dataCollection_dict = full_dict[_dc_key]
    dataCollection_list = dataCollection_dict[_dc_list_key]

    # extract dataCollection - fx and ccy.
    # two empty dicts with list values
     # loop through each sorting into fx and currency dicts
    fx_dict = defaultdict(list)
    ccy_dict = defaultdict(list)
    for dataCollection_set in dataCollection_list:
        dataCollection_res = dataCollection_set.get( _data_1d_key ) or dataCollection_set.get( _datacollection_key )
        dataCollection_key = dataCollection_res[ _dataconv_key ]
        if utils.is_ccypair( dataCollection_key ):
            fx_dict[dataCollection_key].append(dataCollection_res[_datapoint_list_key])
        else:
            ccy = dataCollection_key[ 0:3 ]
            if utils.is_currency(ccy):
                ccy_dict[ccy].append(dataCollection_set)
           
    dataCollection_return_dict = { "fx": fx_dict , "currency" : ccy_dict}
    return dataCollection_return_dict