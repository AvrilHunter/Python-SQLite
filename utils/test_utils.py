from utils.utils import list_to_dict, nested_list_to_dict

def test_list_to_dict():
    headers = ['treasure_id', 'treasure_name', 'colour', 'age', 'cost_at_auction', 'shop_id']
    data = [
		2,
		"treasure-d",
		"azure",
		100,
		1001,
		4
	]
    assert list_to_dict(data, headers) == {'treasure_id':2, 'treasure_name':"treasure-d", 'colour':"azure", 'age':100, 'cost_at_auction':1001, "shop_id":4}
    
def test_nested_list_to_dict():
    headers = ['treasure_id', 'treasure_name', 'colour', 'age', 'cost_at_auction', 'shop_id']
    data = [[
		2,
		"treasure-d",
		"azure",
		100,
		1001,
		4
	],[
		2,
		"treasure-d",
		"azure",
		100,
		1001,
		4
	]]
    assert nested_list_to_dict(data,headers)==[{'treasure_id':2, 'treasure_name':"treasure-d", 'colour':"azure", 'age':100, 'cost_at_auction':1001, "shop_id":4},{'treasure_id':2, 'treasure_name':"treasure-d", 'colour':"azure", 'age':100, 'cost_at_auction':1001, "shop_id":4}]
    