# MinesweeperGit

The first project that i'm 1st year student of Computer Engineering after we learned programming course, the teacher assign the project about "something about programming that we learned" and i love playing minesweeper game of Microsoft windows game so i decide to make this game

Concept(วิธีการเล่น)
1. ตารางขนาด 9*9  (เบื้องต้น)  the table size is 9*9 (in the program we can choose the size)

##8  | XX XX XX XX XX XX XX XX XX |

##7  | XX XX XX XX XX XX XX XX XX |

##6  | XX XX XX XX XX XX XX XX XX |

##5  | XX XX XX XX XX XX XX XX XX |

##4  | XX XX XX XX XX XX XX XX XX |

##3  | XX XX XX XX XX XX XX XX XX |

##2  | XX XX XX XX XX XX XX XX XX |

##1  | XX XX XX XX XX XX XX XX XX |

##0  | XX XX XX XX XX XX XX XX XX |

##   +----------------------------+


2. Random 10 Mines(bomb)  ในตาราง 9*9
3. User เล่นโดย Select ตาราง ห้ามโดน Mine(bomb), the solution is player have to play the game, Don't get the mine
4. ถ้า Sweep แล้วเจอ Mine(bomb) “แพ้ ” If you sweep to get mine that you will lose
5. ถ้า Sweep จนทั้งตาราง 9*9 เหลือแต่ Mine(bomb) “ ชนะ ” If you sweep until all the game board that you win
6. นอกจากนี้ จะมีตัวเลขที่แสดงคือจำนวนระเบิดที่อยู่รอบๆ In addition, the hide of this game is the number when you sweep if it is not a mine the board will show mines amount around that position

GUI (Graphic User Interface)
- Appearance file : สำหรับโชว์ข้อความต่างๆ เช่น เกมชนะ เกมแพ้ หรือข้อผิดพลาดในการกรอกข้อมูล
- Event file : สำหรับควบคุมโปรแกรม
- Main file : สำหรับรันโปรแกรมเพื่อเริ่มเกม โดยรันผ่าน cmd เลือก cd local file เพิ่มคำสั่ง py Main.py

read more : https://sites.google.com/view/janthakool/my-portfolio/programming-project-i
