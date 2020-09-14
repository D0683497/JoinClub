import { UserDetailComponent } from '../user-detail/user-detail.component';
import { User } from '../../models/user/user.model';
import { UserService } from '../../services/user/user.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator, PageEvent, MatPaginatorIntl } from '@angular/material/paginator';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatDialog } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { map, shareReplay } from 'rxjs/operators';

@Component({
  selector: 'app-users-list',
  templateUrl: './users-list.component.html',
  styleUrls: ['./users-list.component.scss']
})
export class UsersListComponent implements OnInit {

  @ViewChild(MatPaginator) paginator: MatPaginator;

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  dataSource = new MatTableDataSource<User>();
  pageIndex = 0;
  pageSize = 10;
  pageLength: number;
  pageSizeOptions: number[] = [10, 20, 30, 40, 50];
  displayedColumns: string[] = ['nid', 'name', 'college', 'department', 'class', 'action'];
  fetchDataError = false;
  loading = true;

  constructor(
    private userService: UserService,
    private snackBar: MatSnackBar,
    private matPaginatorIntl: MatPaginatorIntl,
    private dialog: MatDialog,
    private breakpointObserver: BreakpointObserver) { }

  ngOnInit(): void {
    this.getData();
    this.initPaginator();
  }

  onPageChange(event: PageEvent): void {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.getData();
  }

  getData(): void {
    this.userService.getAllItemsLength().subscribe(
      data => { this.pageLength = data; }
    );
    this.userService.getAllUsers(this.pageIndex + 1, this.pageSize).subscribe(
      data => {
        this.dataSource.data = data;
        this.fetchDataError = false;
        this.loading = false;
      },
      error => {
        this.snackBar.open('獲取資料失敗', '關閉', { duration: 5000 });
        this.fetchDataError = true;
        this.loading = false;
      }
    );
  }

  reload(): void {
    this.fetchDataError = false;
    this.loading = true;
    this.ngOnInit();
  }

  showDetailDialog(user: User): void {
    const dialogRef = this.dialog.open(UserDetailComponent, {data: user});
    dialogRef.afterClosed().subscribe(() => {
      this.ngOnInit();
    });
  }

  initPaginator(): void {
    this.matPaginatorIntl.getRangeLabel = (page: number, pageSize: number, length: number): string => {
      return `第 ${page + 1} / ${Math.ceil(length / pageSize)} 頁`;
    };
    this.matPaginatorIntl.itemsPerPageLabel = '每頁筆數：';
    this.matPaginatorIntl.nextPageLabel = '下一頁';
    this.matPaginatorIntl.previousPageLabel = '上一頁';
    this.matPaginatorIntl.firstPageLabel = '第一頁';
    this.matPaginatorIntl.lastPageLabel = '最後一頁';
  }

}
