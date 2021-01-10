print('beginning outer loop')
for outer_loop_counter in range(0, 10):
	print('beginning inner loop')
	for inner_loop_counter in range(0, 10):
		print('[{}] [{}]'.format(outer_loop_counter, inner_loop_counter))
	print('end of inner loop')
print('end of outer loop')