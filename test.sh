echo "this is CICD"
echo " test file" > test.txt
ls -l > list.txt

echo " new line: $(date)"
echo " after CICD" >> test.txt
echo " last check" >> test.txt
