import pandas
import datetime

def scraping_yahoo(code, start, end, term):
	base = "http://info.finance.yahoo.co.jp/history/?code={0}.T&{1}&{2}&tm={3}&p={4}"

	start = str(start)
	start = start.split("-")
	start = "sy={0}&sm={1}&sd={2}".format(start[0], start[1], start[2])
	end = str(end)
	end = end.split("-")
	end = "ey={0}&em={1}&ed={2}".format(end[0], end[1], end[2])
	page = 1

	result = []
	while True:
		url = base.format(code, start, end, term, page)
		df = pandas.read_html(url, header=0)
		if len(df[1]) == 0:
			break

		result.append(df[1])
		page += 1
	result = pandas.concat(result)
	result.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']

	return result


if __name__ == "__main__":
	company = 4312

	EndDate = datetime.date.today()
	StartDate = EndDate - datetime.timedelta(days=30)

	data = scraping_yahoo(company, StartDate, EndDate, "d")
	print(data)
