add <- function(x,y){
    x + y
}

print(add(1,2))

h <- c(1,2,3,4,5)
M <- c("A","B","C","D","E")
barplot(h,names.arg = M, xlab = "X", ylab = "Y")