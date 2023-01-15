# Program that takes path to a local Github repo as cmnd line argument
# Prints facts about the repository
import sys
import git
import time

def main():
	# Check for proper input
	if (len(sys.argv) != 2):
		print("Error: Program is intended to take one file path as an argument")
		return
	git_dir = sys.argv[1]

	# Check if the path exists and is a git repo
	if os.path.exists(git_dir):
  		try:
  			git_inspect(git_dir)
  		except:
  			print("Error: Directory is not a git repository")
	else:
  		print("Error: The path '{}' does not exist.".format(git_dir))

def git_inspect(git_dir):
	# Create repo object
	repo = git.Repo(git_dir)
	# Print active branch
	print("active branch:", repo.active_branch)
	# Check whether repository files have been modified
	print("local changes:", repo.is_dirty(untracked_files=True))
	# Check whether the current head commit was authored in the last week
	time_change = True if (round(time.time()) - repo.head.commit.committed_date < 60 * 60 * 24 * 7) else False
	print("recent commit: ", time_change)
	# Check whether current head commit was authored by Rufus
	rufus = True if repo.head.commit.author.name == "Rufus" else False
	print("blame Rufus:", rufus)

main()