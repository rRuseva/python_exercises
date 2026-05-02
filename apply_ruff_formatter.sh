file="$1"
echo ""
echo "apply ruff with line-length=120"
ruff format "$file" --line-length=120