using AMD
using DelimitedFiles
using SparseArrays

mat = readdlm("matrix.csv", ',', Float64)
mat = reshape(mat, 450, 450)
p = amd(sparse(mat))
writedlm("permutation.csv", p, ',')
