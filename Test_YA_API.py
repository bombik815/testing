from TEST.Api_yandex import YaDisk

def test_get_f_list():
    """ Введите свой токен от Яндекс Диска!
        Пример : token_your ='###AAAAWLmw########ud0lyl25M####'
    """
    token_your ='###AAAAWLmw########ud0lyl25M####'
    rs = YaDisk(token_your)
    assert 200 == rs.get_f_list()

def test_upload_file_to_disk():
    """
    Введите имя папки которую необходимо создать на Яндекс диске
    Пример: name_folder='имя_папки'
    Пример : token_your ='###AAAAWLmw########ud0lyl25M####'
    :return: код ответа запроса 201 - Успех (папка создалась)
    """
    name_folder = '222'
    token_your = '###AAAAWLmw########ud0lyl25M####'
    rs = YaDisk(token_your)
    assert rs.upload_file_to_disk(name_folder)== 201

