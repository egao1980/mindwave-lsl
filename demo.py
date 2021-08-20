from mindwavelsl import MindwaveLSL

mwlsl = MindwaveLSL('localhost', 13854, file_outlet_path='out')

# Setup the LSL outlet and the ThinkGear connection
mwlsl.setup()
mwlsl.write('{"enableRawOutput": true, "format": "Json"}')

# Run the service
mwlsl.run()
