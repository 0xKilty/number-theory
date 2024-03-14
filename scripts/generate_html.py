import git

repo = git.Repo("..")
main_branch = repo.commit("main")
tree = main_branch.tree

for blob in tree.traverse():
    if blob.type == 'blob':
        print(blob.path)
