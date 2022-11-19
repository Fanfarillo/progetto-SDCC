// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Discovery.proto

package control.proto;

/**
 * Protobuf type {@code proto.microserviceInfoReply}
 */
public  final class microserviceInfoReply extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:proto.microserviceInfoReply)
    microserviceInfoReplyOrBuilder {
private static final long serialVersionUID = 0L;
  // Use microserviceInfoReply.newBuilder() to construct.
  private microserviceInfoReply(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private microserviceInfoReply() {
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return this.unknownFields;
  }
  private microserviceInfoReply(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    this();
    if (extensionRegistry == null) {
      throw new java.lang.NullPointerException();
    }
    int mutable_bitField0_ = 0;
    com.google.protobuf.UnknownFieldSet.Builder unknownFields =
        com.google.protobuf.UnknownFieldSet.newBuilder();
    try {
      boolean done = false;
      while (!done) {
        int tag = input.readTag();
        switch (tag) {
          case 0:
            done = true;
            break;
          case 10: {
            control.proto.infoMicroservices.Builder subBuilder = null;
            if (microservices_ != null) {
              subBuilder = microservices_.toBuilder();
            }
            microservices_ = input.readMessage(control.proto.infoMicroservices.parser(), extensionRegistry);
            if (subBuilder != null) {
              subBuilder.mergeFrom(microservices_);
              microservices_ = subBuilder.buildPartial();
            }

            break;
          }
          default: {
            if (!parseUnknownFieldProto3(
                input, unknownFields, extensionRegistry, tag)) {
              done = true;
            }
            break;
          }
        }
      }
    } catch (com.google.protobuf.InvalidProtocolBufferException e) {
      throw e.setUnfinishedMessage(this);
    } catch (java.io.IOException e) {
      throw new com.google.protobuf.InvalidProtocolBufferException(
          e).setUnfinishedMessage(this);
    } finally {
      this.unknownFields = unknownFields.build();
      makeExtensionsImmutable();
    }
  }
  public static final com.google.protobuf.Descriptors.Descriptor
      getDescriptor() {
    return control.proto.Discovery.internal_static_proto_microserviceInfoReply_descriptor;
  }

  @java.lang.Override
  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return control.proto.Discovery.internal_static_proto_microserviceInfoReply_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            control.proto.microserviceInfoReply.class, control.proto.microserviceInfoReply.Builder.class);
  }

  public static final int MICROSERVICES_FIELD_NUMBER = 1;
  private control.proto.infoMicroservices microservices_;
  /**
   * <code>.proto.infoMicroservices microservices = 1;</code>
   */
  public boolean hasMicroservices() {
    return microservices_ != null;
  }
  /**
   * <code>.proto.infoMicroservices microservices = 1;</code>
   */
  public control.proto.infoMicroservices getMicroservices() {
    return microservices_ == null ? control.proto.infoMicroservices.getDefaultInstance() : microservices_;
  }
  /**
   * <code>.proto.infoMicroservices microservices = 1;</code>
   */
  public control.proto.infoMicroservicesOrBuilder getMicroservicesOrBuilder() {
    return getMicroservices();
  }

  private byte memoizedIsInitialized = -1;
  @java.lang.Override
  public final boolean isInitialized() {
    byte isInitialized = memoizedIsInitialized;
    if (isInitialized == 1) return true;
    if (isInitialized == 0) return false;

    memoizedIsInitialized = 1;
    return true;
  }

  @java.lang.Override
  public void writeTo(com.google.protobuf.CodedOutputStream output)
                      throws java.io.IOException {
    if (microservices_ != null) {
      output.writeMessage(1, getMicroservices());
    }
    unknownFields.writeTo(output);
  }

  @java.lang.Override
  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    if (microservices_ != null) {
      size += com.google.protobuf.CodedOutputStream
        .computeMessageSize(1, getMicroservices());
    }
    size += unknownFields.getSerializedSize();
    memoizedSize = size;
    return size;
  }

  @java.lang.Override
  public boolean equals(final java.lang.Object obj) {
    if (obj == this) {
     return true;
    }
    if (!(obj instanceof control.proto.microserviceInfoReply)) {
      return super.equals(obj);
    }
    control.proto.microserviceInfoReply other = (control.proto.microserviceInfoReply) obj;

    boolean result = true;
    result = result && (hasMicroservices() == other.hasMicroservices());
    if (hasMicroservices()) {
      result = result && getMicroservices()
          .equals(other.getMicroservices());
    }
    result = result && unknownFields.equals(other.unknownFields);
    return result;
  }

  @java.lang.Override
  public int hashCode() {
    if (memoizedHashCode != 0) {
      return memoizedHashCode;
    }
    int hash = 41;
    hash = (19 * hash) + getDescriptor().hashCode();
    if (hasMicroservices()) {
      hash = (37 * hash) + MICROSERVICES_FIELD_NUMBER;
      hash = (53 * hash) + getMicroservices().hashCode();
    }
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static control.proto.microserviceInfoReply parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.microserviceInfoReply parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.microserviceInfoReply parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static control.proto.microserviceInfoReply parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static control.proto.microserviceInfoReply parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static control.proto.microserviceInfoReply parseFrom(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }

  @java.lang.Override
  public Builder newBuilderForType() { return newBuilder(); }
  public static Builder newBuilder() {
    return DEFAULT_INSTANCE.toBuilder();
  }
  public static Builder newBuilder(control.proto.microserviceInfoReply prototype) {
    return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
  }
  @java.lang.Override
  public Builder toBuilder() {
    return this == DEFAULT_INSTANCE
        ? new Builder() : new Builder().mergeFrom(this);
  }

  @java.lang.Override
  protected Builder newBuilderForType(
      com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
    Builder builder = new Builder(parent);
    return builder;
  }
  /**
   * Protobuf type {@code proto.microserviceInfoReply}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:proto.microserviceInfoReply)
      control.proto.microserviceInfoReplyOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return control.proto.Discovery.internal_static_proto_microserviceInfoReply_descriptor;
    }

    @java.lang.Override
    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return control.proto.Discovery.internal_static_proto_microserviceInfoReply_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              control.proto.microserviceInfoReply.class, control.proto.microserviceInfoReply.Builder.class);
    }

    // Construct using control.proto.microserviceInfoReply.newBuilder()
    private Builder() {
      maybeForceBuilderInitialization();
    }

    private Builder(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      super(parent);
      maybeForceBuilderInitialization();
    }
    private void maybeForceBuilderInitialization() {
      if (com.google.protobuf.GeneratedMessageV3
              .alwaysUseFieldBuilders) {
      }
    }
    @java.lang.Override
    public Builder clear() {
      super.clear();
      if (microservicesBuilder_ == null) {
        microservices_ = null;
      } else {
        microservices_ = null;
        microservicesBuilder_ = null;
      }
      return this;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return control.proto.Discovery.internal_static_proto_microserviceInfoReply_descriptor;
    }

    @java.lang.Override
    public control.proto.microserviceInfoReply getDefaultInstanceForType() {
      return control.proto.microserviceInfoReply.getDefaultInstance();
    }

    @java.lang.Override
    public control.proto.microserviceInfoReply build() {
      control.proto.microserviceInfoReply result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    @java.lang.Override
    public control.proto.microserviceInfoReply buildPartial() {
      control.proto.microserviceInfoReply result = new control.proto.microserviceInfoReply(this);
      if (microservicesBuilder_ == null) {
        result.microservices_ = microservices_;
      } else {
        result.microservices_ = microservicesBuilder_.build();
      }
      onBuilt();
      return result;
    }

    @java.lang.Override
    public Builder clone() {
      return (Builder) super.clone();
    }
    @java.lang.Override
    public Builder setField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return (Builder) super.setField(field, value);
    }
    @java.lang.Override
    public Builder clearField(
        com.google.protobuf.Descriptors.FieldDescriptor field) {
      return (Builder) super.clearField(field);
    }
    @java.lang.Override
    public Builder clearOneof(
        com.google.protobuf.Descriptors.OneofDescriptor oneof) {
      return (Builder) super.clearOneof(oneof);
    }
    @java.lang.Override
    public Builder setRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        int index, java.lang.Object value) {
      return (Builder) super.setRepeatedField(field, index, value);
    }
    @java.lang.Override
    public Builder addRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return (Builder) super.addRepeatedField(field, value);
    }
    @java.lang.Override
    public Builder mergeFrom(com.google.protobuf.Message other) {
      if (other instanceof control.proto.microserviceInfoReply) {
        return mergeFrom((control.proto.microserviceInfoReply)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(control.proto.microserviceInfoReply other) {
      if (other == control.proto.microserviceInfoReply.getDefaultInstance()) return this;
      if (other.hasMicroservices()) {
        mergeMicroservices(other.getMicroservices());
      }
      this.mergeUnknownFields(other.unknownFields);
      onChanged();
      return this;
    }

    @java.lang.Override
    public final boolean isInitialized() {
      return true;
    }

    @java.lang.Override
    public Builder mergeFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      control.proto.microserviceInfoReply parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (control.proto.microserviceInfoReply) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }

    private control.proto.infoMicroservices microservices_ = null;
    private com.google.protobuf.SingleFieldBuilderV3<
        control.proto.infoMicroservices, control.proto.infoMicroservices.Builder, control.proto.infoMicroservicesOrBuilder> microservicesBuilder_;
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public boolean hasMicroservices() {
      return microservicesBuilder_ != null || microservices_ != null;
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public control.proto.infoMicroservices getMicroservices() {
      if (microservicesBuilder_ == null) {
        return microservices_ == null ? control.proto.infoMicroservices.getDefaultInstance() : microservices_;
      } else {
        return microservicesBuilder_.getMessage();
      }
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public Builder setMicroservices(control.proto.infoMicroservices value) {
      if (microservicesBuilder_ == null) {
        if (value == null) {
          throw new NullPointerException();
        }
        microservices_ = value;
        onChanged();
      } else {
        microservicesBuilder_.setMessage(value);
      }

      return this;
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public Builder setMicroservices(
        control.proto.infoMicroservices.Builder builderForValue) {
      if (microservicesBuilder_ == null) {
        microservices_ = builderForValue.build();
        onChanged();
      } else {
        microservicesBuilder_.setMessage(builderForValue.build());
      }

      return this;
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public Builder mergeMicroservices(control.proto.infoMicroservices value) {
      if (microservicesBuilder_ == null) {
        if (microservices_ != null) {
          microservices_ =
            control.proto.infoMicroservices.newBuilder(microservices_).mergeFrom(value).buildPartial();
        } else {
          microservices_ = value;
        }
        onChanged();
      } else {
        microservicesBuilder_.mergeFrom(value);
      }

      return this;
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public Builder clearMicroservices() {
      if (microservicesBuilder_ == null) {
        microservices_ = null;
        onChanged();
      } else {
        microservices_ = null;
        microservicesBuilder_ = null;
      }

      return this;
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public control.proto.infoMicroservices.Builder getMicroservicesBuilder() {
      
      onChanged();
      return getMicroservicesFieldBuilder().getBuilder();
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    public control.proto.infoMicroservicesOrBuilder getMicroservicesOrBuilder() {
      if (microservicesBuilder_ != null) {
        return microservicesBuilder_.getMessageOrBuilder();
      } else {
        return microservices_ == null ?
            control.proto.infoMicroservices.getDefaultInstance() : microservices_;
      }
    }
    /**
     * <code>.proto.infoMicroservices microservices = 1;</code>
     */
    private com.google.protobuf.SingleFieldBuilderV3<
        control.proto.infoMicroservices, control.proto.infoMicroservices.Builder, control.proto.infoMicroservicesOrBuilder> 
        getMicroservicesFieldBuilder() {
      if (microservicesBuilder_ == null) {
        microservicesBuilder_ = new com.google.protobuf.SingleFieldBuilderV3<
            control.proto.infoMicroservices, control.proto.infoMicroservices.Builder, control.proto.infoMicroservicesOrBuilder>(
                getMicroservices(),
                getParentForChildren(),
                isClean());
        microservices_ = null;
      }
      return microservicesBuilder_;
    }
    @java.lang.Override
    public final Builder setUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.setUnknownFieldsProto3(unknownFields);
    }

    @java.lang.Override
    public final Builder mergeUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.mergeUnknownFields(unknownFields);
    }


    // @@protoc_insertion_point(builder_scope:proto.microserviceInfoReply)
  }

  // @@protoc_insertion_point(class_scope:proto.microserviceInfoReply)
  private static final control.proto.microserviceInfoReply DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new control.proto.microserviceInfoReply();
  }

  public static control.proto.microserviceInfoReply getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<microserviceInfoReply>
      PARSER = new com.google.protobuf.AbstractParser<microserviceInfoReply>() {
    @java.lang.Override
    public microserviceInfoReply parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return new microserviceInfoReply(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<microserviceInfoReply> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<microserviceInfoReply> getParserForType() {
    return PARSER;
  }

  @java.lang.Override
  public control.proto.microserviceInfoReply getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

