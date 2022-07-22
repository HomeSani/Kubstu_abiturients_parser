import json
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_abiturents(driver, facultet):
	driver.get(facultet[-1])

	json_string = driver.find_element(By.TAG_NAME, "body").text
	json_list = json.loads(json_string)

	abiturients = []
	for abiturient_item in json_list["roll"]:
		abiturient = [int(abiturient_item[-1]), abiturient_item[1], abiturient_item[-2]]
		abiturients.append(abiturient)

	return sorted(abiturients, reverse=True)


def save_data_in_csv(abiturients, facultet):
	f = open(facultet[0] + ".csv", "w")
	writer = csv.writer(f)

	writer.writerow(["Номер", "Имя", "Баллы", "Солгасие"])

	i = 1
	for abiturient in abiturients:
		line = []

		if abiturient[-1] == 0:
			line = [i, abiturient[1], abiturient[0], "Не подано"]
		else:
			line = [i, abiturient[1], abiturient[0], "ПОДАНО"]

		writer.writerow(line)

		i += 1

	f.close()


def main():
	facultets = [
		["Информатика и вычислительная техика", "https://ent.kubstu.ru/?rank=0&edlv=2&edfm=1&estp=1&hid=5&fid=516&id=14038&psm=0"],
		["Прикладная информатика", "https://ent.kubstu.ru/?rank=0&edlv=2&edfm=1&estp=1&hid=5&fid=516&id=14040&psm=0"],
		["Информационная безопасность", "https://ent.kubstu.ru/?rank=0&edlv=2&edfm=1&estp=1&hid=5&fid=516&id=14104&psm=0"],
		["Программная инженерия", "https://ent.kubstu.ru/?rank=0&edlv=2&edfm=1&estp=1&hid=5&fid=516&id=14041&psm=0"],
		["Автоматизация технологических процессов и производств", "https://ent.kubstu.ru/?rank=0&edlv=2&edfm=1&estp=1&hid=5&fid=539&id=14758&psm=0"],
	]

	driver = webdriver.Chrome()

	for facultet in facultets:
		abiturients = get_abiturents(driver, facultet)
		save_data_in_csv(abiturients, facultet)

	driver.close()


if __name__ == '__main__':
	main()