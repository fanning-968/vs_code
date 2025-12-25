import json
def main():
    mydict = {
        'name' : '樊宁',
        'age' : 28,
        'qq' : 1552730303,
        'friends' : ['王大锤', '李白'],
        'cars' : [
            {'brand' : 'byd', 'max_speed' : '180'},
            {'brand' : 'audi', 'max_speed' : '280'}
        ]
    }

    ha = json.dumps(mydict)
    print(type(ha))
    # try:
    #     with open ('data.json', 'w', encoding='utf-8') as fs:
    #         json.dump(mydict, fs)
    # except IOError as e:
    #     print(e)
    # print('保存数据完成')

if __name__ == '__main__':
    main()
