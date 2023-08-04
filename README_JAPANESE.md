# Augmented World Backend API Server

## 概要

ウェブアプリケーション「Augmented World」のサーバーサイドリポジトリです。Django REST Framework（DRF）アプリケーションです。

使用されるテックスタックには、Python、Django、Django REST Framework、データベースのための PostgreSQL、ホスティングとストレージのための Google Cloud、コンテナ化のための Docker となります。

## テックスタック

- Python
- Django
- Django REST Framework
- PostgreSQL
- Google Cloud
- Docker
- GitHub Actions for CI/CD (作成中)

## データベース

データベースは、PostgreSQL を使用しています。

## テスト (作成中)

単体テストと統合テストは'tests'ディレクトリに含まれています。

## CI/CD (作成中)

GitHub Actions は継続的な統合とデプロイのために使用されます。ワークフローの設定については.github/workflows/main.yml を参照してください。リポジトリにプッシュするたびに、アクションがトリガーされ、アプリケーションが正しくビルドされ、すべてのテストがパスすることを確認します。

## フロントエンド

このアプリケーションのフロントエンドのコードベースは、次のリポジトリで公開しております: https://github.com/yurite6174/augmented-world-website. React/Next.js をベースとした Web アプリケーションです。

## 貢献

貢献は歓迎されます。リポジトリをフォークし、変更点をプルリクエストで作成してください。

## ライセンス

このプロジェクトは MIT ライセンスのもとでライセンスされています - 詳細は LICENSE ファイルをご覧ください。

追加の質問やコメントがある場合は、このリポジトリで問題を開いてください。
