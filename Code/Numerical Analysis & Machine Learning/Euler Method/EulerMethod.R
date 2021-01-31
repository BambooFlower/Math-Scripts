# Implementation of Euler's method

f <- function(ti,y) y

# INITIAL VALUES:
t0 <- 0
y0 <- 1
h  <- 1
tn <- 4

# Euler's method: function definition
Euler <- function(t0, y0, h, tn, dy.dt) {
  # dy.dt: derivative function
  
  # t sequence:
  tt <- seq(t0, tn, by=h)
  # table with as many rows as tt elements:
  tbl <- data.frame(ti=tt)
  tbl$yi <- y0 # Initializes yi with y0
  tbl$Dy.dt[1] <- dy.dt(tbl$ti[1],y0) # derivative
  for (i in 2:nrow(tbl)) {
    tbl$yi[i] <- tbl$yi[i-1] + h*tbl$Dy.dt[i-1]
    # For next iteration:
    tbl$Dy.dt[i] <- dy.dt(tbl$ti[i],tbl$yi[i])
  }
  return(tbl)
}

# Euler's method: function application
r <- Euler(t0, y0, h, tn, f)
rownames(r) <- 0:(nrow(r)-1) # to coincide with index n

# Exact solution for this case: y = exp(t)
#       added as an additional column to r
r$y <- exp(r$ti)

# TABLE with results:
print(r)

plot(r$ti, r$y, type="l", col="red", lwd=2)
lines(r$ti, r$yi, col="blue", lwd=2)
grid(col="black")
legend("top",  legend = c("Exact", "Euler"), lwd=2,  col = c("red", "blue"))