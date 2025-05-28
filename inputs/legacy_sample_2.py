# legacy_complex_sample.py

print "Starting legacy script..."

class DataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = {}

    def load_data(self):
        f = open(self.data_file)
        for line in f:
            if line.strip():
                key, value = line.strip().split(',')
                self.data[key] = int(value)
        f.close()

    def process_data(self):
        print "Processing data..."
        for key, value in self.data.iteritems():
            self.data[key] = value * 2

    def save_results(self, output_file):
        try:
            f = open(output_file, 'w')
            for key in self.data:
                f.write("%s,%d\n" % (key, self.data[key]))
            f.close()
        except IOError, e:
            print "Error writing file:", e

def generate_report(numbers):
    print "Generating report..."
    total = 0
    for i in xrange(len(numbers)):
        total += numbers[i]
    average = total / len(numbers)
    print "Total:", total
    print "Average:", average

if __name__ == "__main__":
    processor = DataProcessor("input_data.csv")
    processor.load_data()
    processor.process_data()
    processor.save_results("output_results.csv")

    nums = [5, 10, 15, 20, 25]
    generate_report(nums)

print ("Script finished.")
