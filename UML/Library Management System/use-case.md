# Use case

## System

- Library

## Primary Actors

- Member
- Librarian

## Secondary Actors

- System(Library)

## Use cases

### Librarian

- Add book: To add a new book to the library
- Remove book: To remove an existing book from the library
- Edit book: To modify a book(book details)
- Register new account: To register a new library member
- Cancel membership: To cancel the library membership of a member
- Register/Update Account: To create or update any member's account
- Login/Logout: To log in or log out account
- Issue book: To issue a book to a member
- Remove reservation: To remove reservation of books
- Renew Books: To renew the issuance of the book
- Reserve book: To reserve a book that is currently not available
- View account: To view the account and access all account details

### Member

- Search Catalog: To search a book in the library
- Cancel memberships: To cancel the self library membership
- Register/Update Account: To create or update self account
- Login/Logout: To log in or log out account
- Remove Reservation: To remove reservation of books
- Renew Books: To renew the issuance of the book
- Reserve book: To reserve a book that is currently not available
- View account: To view the account and access self account details
- Checkout book: To complete the issue book process
- Return book: To return a book to the library

### System (Secondary Actor)

- Overdue notification: To send an alert if the book is not returned on time
- Reservation available notification: To send an alert when the book is available for reservation
- Reservation cancelled notification: To send an alert when a book reservation is canceled

### Extras

- Add book item: To add an item of a book in the catalog

- Edit book item: To edit the details of a book item in a catalog

- Remove book item: To remove a book item from the catalog

- Update catalog: To update (add, edit, or remove) a book item or book from the catalog

- Issue library card: To issue a library card to new members that will be for identification.

- By subject name: To search for a book in the catalog by its subject name

- By book title: To search for a book in the catalog by its title

- By author name: To search for a book in the catalog by its author name

- By publication date: To search for a book in the catalog by its publication date

- Pay fine: To pay a fine if the book is returned after the due date

## Generalization

We can search for a book with the title, subject name, author name, or publication date. This shows that the “Search catalog” use case has a generalization relationship with “By subject name,” “By book title,” “By author name,” and “By publication date” use cases.

## Association

- all the above mentioned use cases

## Include

- To add a new book, we add its copies (book items), so the "Add Book" use case has an include relationship with the "Add book item" use case.

- To edit a book, we need to edit its items, so the "Edit Book" use case has an include relationship with the "Edit book item" use case.

- To remove a book from the library, we need to remove its items, so the "Remove Book" use case has an include relationship with the "Remove book item" use case.

- To update a catalog, we need to update all the book items. This will include adding, editing, or removing a book item since “Edit book item,” “Add book item,” and “Remove book item” have an include relationship with the “Update catalog” use case.

- To issue a book, we need to go through a checkout process, so the “issue book” use case has an include relationship with the “Checkout book” use case.

- Whenever we go through the checkout process, our book reservation will be removed as it had been issued. So the "Checkout book" use case has an include relationship with the "Remove reservation" use case.

## Extend

- When a new member is registered, a library card is issued. So the "Register new member" use case has an extend relationship with the "Issue library card" use case.

- Whenever a member returns a book, the librarian will check if the submission is late or not and will ask the member to pay for a fine if it exists, so the "Return book" use case has an extend relationship with "Pay fine" use case.

## Diagram

::: mermaid
graph LR

  M[Member]
  L[Librarian]
  S[System]

  M --> u1[Login/Logout]
  M --> u2[Search Catalog]
  M --> u3[Register/Update Account]
  M --> u4[Remove Reservation]
  M --> u5[Renew Books]
  M --> u6[Reserve Book]
  M --> u7[View account]
  M --> u8[Checkout book]
  M --> u9[Return book]

  S --> u10[overdue notification]
  S --> u11[Reservation available notification]
  S --> u12[Reservation cancelled notification]

  L --> u13[Add book]
  L --> u14[Remove book]
  L --> u15[Edit book]
  L --> u16[Register new account]
  L --> u17[Cancel membership]
  L --> u3
  L --> u1
  L --> u18[Issue book]
  L --> u4
  L --> u5
  L --> u6
  L --> u7

  u19[Add book item]
  u20[Edit book item]
  u21[Remove book item]
  u22[Update catalog]
  u23[Issue library card]
  u24[By subject name]
  u25[By book title]
  u26[By author name]
  u27[By publication date]
  u28[Pay fine]

  u24 --> u2
  u25 --> u2
  u26 --> u2
  u27 --> u2

  u13 -.include.-> u19
  u14 -.include.-> u21
  u15 -.include.-> u20

  u19 -.include.-> u22
  u20 -.include.-> u22
  u21 -.include.-> u22

  u18 -.include.-> u8
  u8 -.include.-> u4

  u23 -.extend.-> u16
  u28  -.extend.-> u9
:::
