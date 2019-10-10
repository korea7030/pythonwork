from diff_match_patch import diff_match_patch, patch_obj

textA = "the cat in the red hat"
textB = "the feline in the blue hat"
textC = "the cet in the rad hat"

#create a diff_match_patch object
dmp = diff_match_patch()

# Depending on the kind of text you work with, in term of overall length
# and complexity, you may want to extend (or here suppress) the
# time_out feature
dmp.Diff_Timeout = 0   # or some other value, default is 1.0 seconds

# All 'diff' jobs start with invoking diff_main()
diffs = dmp.diff_main(textA, textB)
diffs2 = dmp.diff_main(textA, textC) ## check

text_array = dmp.diff_linesToChars(textA, textC)
overlap = dmp.diff_commonOverlap(textA, textC)

print(dmp.diff_cleanupMerge(diffs2))
print(diffs2)
print(dmp.diff_prettyHtml(diffs2)) ## check

patchs = dmp.patch_make(textA, textC)

print(dmp.patch_apply(patchs, textA))

# and if you want the results as some ready to display HMTL snippet
htmlSnippet = dmp.diff_prettyHtml(diffs)
import re
re.split()