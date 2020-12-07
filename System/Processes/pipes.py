import os, sys

def spawn(prog, *args):
	stdinFd = sys.stdin.fileno()
	stdoutFd = sys.stdout.fileno()

	parentStdin, childStdout = os.pipe()
	childstdIn, parentStdout = os.pipe()
	pid = os.fork()