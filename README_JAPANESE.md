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
- GitHub Actions for CI/CD

## データベース

データベースは、PostgreSQL を使用しています。

## テスト 

単体テストと統合テストコードは各 app folder の'tests'ディレクトリ内にあります。

## CI/CD

GitHub Actions を継続的な統合とデプロイのために使用しています。ワークフローの設定については.github/workflows/ci_cd.yml を参照してください。

## フロントエンド

このアプリケーションのフロントエンドのコードベースは、次のリポジトリで公開しております: https://github.com/yurite6174/augmented-world-website. React/Next.js をベースとした Web アプリケーションです。

## ライセンス

このプロジェクトは MIT ライセンスのもとでライセンスされています - 詳細は LICENSE ファイルをご覧ください。

追加の質問やコメントがある場合は、このリポジトリで issue を開いてください。
