package main

import (
    "bufio"
    "bytes"
    "encoding/binary"
    "fmt"
    "golang.org/x/net/html"
    "io"
    "os"
    "strconv"
)

func bytesToUint(b []byte) uint32 {
    return binary.LittleEndian.Uint32(b)
}

func getHTML() []byte {
    in := bufio.NewReader(os.Stdin)
    first := make([]byte, 4)
    in.Read(first)
    len := bytesToUint(first)
    buf := make([]byte, len)
    io.ReadFull(in, buf)
    return buf
}

func containshref(attr []html.Attribute) bool {
    for _, a := range attr {
        if a.Key == "href" {
            return true
        }
    }
    return false
}

func findlinks(n *html.Node) uint {
    var count uint = 0
    if n.Type == html.ElementNode && n.Data == "a" && containshref(n.Attr) {
        count = 1
    }
    for c := n.FirstChild; c != nil; c = c.NextSibling {
        count += findlinks(c)
    }
    return count
}

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage:", os.Args[0], "<repeats>")
        return
    }

    repeats, err := strconv.Atoi(os.Args[1]);
    if err != nil {
        fmt.Println("Could not convert", os.Args[0], "to number")
        return
    }
    htmlbytes := getHTML()

    for i := 0; i < repeats-1; i++ {
        reader := bytes.NewReader(htmlbytes)
        html.Parse(reader)
    }

    reader := bytes.NewReader(htmlbytes)
    doc, _ := html.Parse(reader)
    fmt.Print(findlinks(doc))
}