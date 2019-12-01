python run.py --build
cd build
git add .
export COMMIT_MESSAGE_DATE_STRING=$(date)
git commit -m "$COMMIT_MESSAGE_DATE_STRING - site update"
git push
cd ..
