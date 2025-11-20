import numpy as np

current_tool = "teeth"
money_per_job = 1
money_in_bank_account = 0
inventory = np.array(["teeth"])
win_condition_met = False

def buy_tool(money_in_bank: int, tool: str, tool_price: int, job_money: int, inventory):
    money_in_bank_account = pay_for_tool(money_in_bank, tool_price)
    price_of_tool = tool_price
    current_tool = tool
    inventory = np.append(inventory, tool)
    money_per_job = job_money

    return money_in_bank_account, price_of_tool, current_tool, inventory, money_per_job

def pay_for_tool(money_in_bank: int, tool_price: int):
    money_in_bank = int(money_in_bank) - int(tool_price)
    return money_in_bank

while win_condition_met == False:
    print(f"You have {money_in_bank_account} money in the bank; your current tool is {current_tool}; your inventory is {inventory}")
    user_wants_to_work = True if input(f"Press 'y' if want to cut lawn with {current_tool} for {money_per_job} money? (bank account: {money_in_bank_account} money) ") == 'y' else False
    
    if user_wants_to_work:
        money_in_bank_account = money_in_bank_account + money_per_job
        print(f"You earned {money_per_job} money")

    if money_in_bank_account >= 5 and "scissors" not in inventory: 
        user_wants_to_buy_scissors = True if input("Press 'y' if you want to buy scissors. ") == 'y' else False

        if user_wants_to_buy_scissors == True:
            price_of_tool = 5
            tool_to_buy = "scissors"
            money_per_job = 5
            money_in_bank_account, price_of_tool, current_tool, inventory, money_per_job = buy_tool(money_in_bank_account, tool_to_buy, price_of_tool, money_per_job, inventory)

    if money_in_bank_account >= 25 and "push-mower" not in inventory: 
        user_wants_to_buy_pushmowever = True if input("Press 'y' if you want to buy push-mower. ") == 'y' else False

        if user_wants_to_buy_pushmowever == True:
            price_of_tool = 25
            tool_to_buy = "push-mower"
            money_per_job = 50
            money_in_bank_account, price_of_tool, current_tool, inventory, money_per_job = buy_tool(money_in_bank_account, tool_to_buy, price_of_tool, money_per_job, inventory)

    if money_in_bank_account >= 250 and "electric-mower" not in inventory: 
        user_wants_to_buy_pushmowever = True if input("Press 'y' if you want to buy electric-mower. ") == 'y' else False

        if user_wants_to_buy_pushmowever == True:
            price_of_tool = 250
            tool_to_buy = "electric-mower"
            money_per_job = 100
            money_in_bank_account, price_of_tool, current_tool, inventory, money_per_job = buy_tool(money_in_bank_account, tool_to_buy, price_of_tool, money_per_job, inventory)

    if money_in_bank_account >= 500 and "students" not in inventory: 
        user_wants_to_buy_pushmowever = True if input("Press 'y' if you want to hire students. ") == 'y' else False

        if user_wants_to_buy_pushmowever == True:
            price_of_tool = 500
            tool_to_buy = "students"
            money_per_job = 250
            money_in_bank_account, price_of_tool, current_tool, inventory, money_per_job = buy_tool(money_in_bank_account, tool_to_buy, price_of_tool, money_per_job, inventory)

    win_condition_met = True if money_in_bank_account >= 1000 and "students" in inventory else False

print("You can retire now")