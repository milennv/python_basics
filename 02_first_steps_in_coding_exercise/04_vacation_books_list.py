number_of_pages = int(input())
read_pages_per_hour = int(input())
days_to_finish_book = int(input())

total_hours_to_read_the_book = number_of_pages / read_pages_per_hour
hours_per_day = total_hours_to_read_the_book / days_to_finish_book

print (int(hours_per_day))
