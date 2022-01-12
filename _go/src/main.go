package main

import (
	"database/sql"
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "admin:park~^^99@tcp(database-1.clt0k54kd7qq.us-east-2.rds.amazonaws.com:3306)/testdb")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// 하나의 Row를 갖는 SQL 쿼리
	//var name string
	ins, err := db.Exec("INSERT INTO testdb2 values (2, 'you')")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(ins)

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pongs",
		})
	})
	r.Run() // listen and serve on 0.0.0.0:8080
}
