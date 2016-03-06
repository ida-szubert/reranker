bleu <- read.csv("param_search", header=TRUE, sep=";")
which(max(bleu$bleu))
plot(NULL, xlim = c(1, 4), ylim = c(24, 28),
     xaxt = "n",
     xlab = "number of features used",
     ylab = "BLEU")



q3 <- read.csv("Q3.txt", header = TRUE, sep = ";")

par(xpd=T, mar=par()$mar+c(0,0,0,4))
plot(NULL, xlim = c(1, 4), ylim = c(24, 28),
     xaxt = "n",
     xlab = "number of features used",
     ylab = "BLEU")
axis(side = 1, at = c(1,2,3,4),
     labels = c("1", "2", "3", "3, one with\nnegative weight"),
     cex.axis = 0.8)
points(3,q3[1,4], pch = 19, col = "orange", cex = 2.5)
points(3,q3[1,4], pch = 19, col = "cyan3", cex = 2)
points(3,q3[1,4], pch = 19, col = "maroon3", cex = 1.5)
# without p(e)
points(2,q3[3,4], pch = 19, col = "cyan3", cex = 2)
points(2,q3[3,4], pch = 19, col = "maroon3", cex = 1.5)
# without p(f|e)
points(2,q3[7,4], pch = 19, col = "orange", cex = 2)
points(2,q3[7,4], pch = 19, col = "maroon3", cex = 1.5)
# without p_lex(e|f)
points(2,q3[11,4], pch = 19, col = "orange", cex = 2)
points(2,q3[11,4], pch = 19, col = "cyan3", cex = 1.5)
# only one
points(1,q3[2,4], pch = 19, col = "orange", cex = 2)
points(1,q3[6,4], pch = 19, col = "cyan3", cex = 2)
points(1,q3[10,4], pch = 19, col = "maroon3", cex = 2)
# reversed
points(4,q3[4,4], pch = 19, col = "black", cex = 2.5)
points(4,q3[4,4], pch = 19, col = "cyan3", cex = 2)
points(4,q3[4,4], pch = 19, col = "maroon3", cex = 1.5)

points(4,q3[8,4], pch = 19, col = "orange", cex = 2.5)
points(4,q3[8,4], pch = 19, col = "black", cex = 2)
points(4,q3[8,4], pch = 19, col = "maroon3", cex = 1.5)

points(4,q3[12,4], pch = 19, col = "orange", cex = 2.5)
points(4,q3[12,4], pch = 19, col = "cyan3", cex = 2)
points(4,q3[12,4], pch = 19, col = "black", cex = 1.5)

legend("topright", inset=c(-0.25,0), c("p(e)", "p(f|e)", "p_lex(e|f)"),
       col=c("orange", "cyan3", "maroon3"),
       bty="n", cex=0.8, pch=19, title="feature")



