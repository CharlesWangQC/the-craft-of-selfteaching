2020年3月8日：学习GIT
克隆现有仓库 $ git clone https://github.com/libgit2/libgit2
检查当前文件状态 $ git status
跟踪新文件 $ git status -s
新添加的未跟踪文件前面有 ?? 标记，新添加到暂存区中的文件前面有 A 标记，修改过的文件前面有 M 标记。 你可能注意到了 M 有两个可以出现的位置，出现在右边的 M 表示该文件被修改了但是还没放入暂存区，出现在靠左边的 M 表示该文件被修改了并放入了暂存区。
跟踪新文件 $ git add README
提交更新 $ git commit
移除文件 $ git rm
移动文件 $ git mv file_from file_to
查看修改历史 $ git log 常用-p选项，用来显示每次提交的内容差异，你也可以加上 -2 来仅显示最近两次提交
撤销操作

git merge 合并两个分支是会产生一个特殊的提交记录，它由两个父节点
git rebase 取出一系列的提交积累，复制他们，然后在另外一个地方逐个的放下去。rebase使你的提交树更干净，所有的提交都在一条线上，缺点修改了提交树的历史。

git HEAD，HEAD是一个对当前检出记录的符号引用，也就是指向你正在其基础上进行工作的提交记录。
使用^向上移动1个提交记录
使用~<num>向上移动多个提交记录，如～3

git reset撤销变更，
git revert HEAD
git reset HEAD～<num> 改写历史，向上移动分支，原来指向的提交记录就跟从来没有提交过一样。

git cherry-pick <提交号>…，将一些提交复制到当前所在的位置（HEAD）下面，该命令是最直接的方式

交互式rebase，指使用带参数—interactive的rebase命令，简写为 -I

git tag 设置版本
git describe 帮你在提交历史中移动了多次以后找到方向。
git describe <ref> 其中<ref>可以是任何能被GIt识别成提交记录的引用，如果你没有指定的话，GIt会以你目前所检出的位置。

git clone
git fetch 从远程仓库获取数据，并不会改变你本地仓库的状态，它不会更新你的master分支，也不会修改你磁盘上的文件
git pull 合并分支
Git push负责将你的变更上传到指定的远程仓库，并在远程仓库上合并你的新提交记录。一旦git push完成，你的朋友们就可以从这个远程仓库下载你分享的成果。
2020年3月10日：尝试提交study