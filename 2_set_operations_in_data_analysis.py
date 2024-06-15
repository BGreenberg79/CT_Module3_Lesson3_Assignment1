# Task 1 Duplicate Entries cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def customer_id_set_conversion(customer_ids):
    set_customer_ids = set(customer_ids)
    print(f"\nThe follwing is the set of Customer ID's without duplicates: {set_customer_ids}")
    print("\nThe following is the same set of customer ID's sorted ascedning:")
    for index, id in enumerate(sorted(set_customer_ids)):
        print(f"{str(index+1)}. {id}")

customer_id_set_conversion(customer_ids)


'''
Cleaning up the list of customer_ids with duplicates was extremely simple as all I needed to do was set up a function where I used the set() function to turn the list into a set
and once it is in a set I know any duplicates will be automatically removed. I printed this result inside the function in an f-string to show that it is a set.
Following me doing that I also ran a for loop with the enumerate function to sort it ascending as the problem statement gave an expected outcome that was sorted ascending and a set without the enumerate function
is unindexed and orderless, so unless I ran the enumerate function I couldn't assure that the result would match the expected output in the problem statement. Using the enumerate function also meant that i decided to house both
print statements inside the function and all I did outside the function was call the function with the original list fed through as the argument.
'''