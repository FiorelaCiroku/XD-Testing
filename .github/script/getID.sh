requirements=$(grep -i '[CQ][0-9][0-9]*:\s' cq.txt)
echo "$requirements" > "requirements.txt"
while read line; do
  echo "${line//[!0-9]/}"
  if [[ $line =~ :(.+) ]]; then
    strresult=${BASH_REMATCH[1]}
    echo "$strresult"
  else
    echo "unable to parse string $line"
  fi
done <requirements.txt
