// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Suggestions.proto

package control.proto;

/**
 * Protobuf type {@code proto.SelectedFlight}
 */
public  final class SelectedFlight extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:proto.SelectedFlight)
    SelectedFlightOrBuilder {
private static final long serialVersionUID = 0L;
  // Use SelectedFlight.newBuilder() to construct.
  private SelectedFlight(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private SelectedFlight() {
    bookingDate_ = "";
    flightDate_ = "";
    airline_ = "";
    departureAirport_ = "";
    arrivalAirport_ = "";
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return this.unknownFields;
  }
  private SelectedFlight(
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
            java.lang.String s = input.readStringRequireUtf8();

            bookingDate_ = s;
            break;
          }
          case 18: {
            java.lang.String s = input.readStringRequireUtf8();

            flightDate_ = s;
            break;
          }
          case 26: {
            java.lang.String s = input.readStringRequireUtf8();

            airline_ = s;
            break;
          }
          case 34: {
            java.lang.String s = input.readStringRequireUtf8();

            departureAirport_ = s;
            break;
          }
          case 42: {
            java.lang.String s = input.readStringRequireUtf8();

            arrivalAirport_ = s;
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
    return control.proto.Suggestions.internal_static_proto_SelectedFlight_descriptor;
  }

  @java.lang.Override
  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return control.proto.Suggestions.internal_static_proto_SelectedFlight_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            control.proto.SelectedFlight.class, control.proto.SelectedFlight.Builder.class);
  }

  public static final int BOOKINGDATE_FIELD_NUMBER = 1;
  private volatile java.lang.Object bookingDate_;
  /**
   * <code>string bookingDate = 1;</code>
   */
  public java.lang.String getBookingDate() {
    java.lang.Object ref = bookingDate_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      bookingDate_ = s;
      return s;
    }
  }
  /**
   * <code>string bookingDate = 1;</code>
   */
  public com.google.protobuf.ByteString
      getBookingDateBytes() {
    java.lang.Object ref = bookingDate_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      bookingDate_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  public static final int FLIGHTDATE_FIELD_NUMBER = 2;
  private volatile java.lang.Object flightDate_;
  /**
   * <code>string flightDate = 2;</code>
   */
  public java.lang.String getFlightDate() {
    java.lang.Object ref = flightDate_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      flightDate_ = s;
      return s;
    }
  }
  /**
   * <code>string flightDate = 2;</code>
   */
  public com.google.protobuf.ByteString
      getFlightDateBytes() {
    java.lang.Object ref = flightDate_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      flightDate_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  public static final int AIRLINE_FIELD_NUMBER = 3;
  private volatile java.lang.Object airline_;
  /**
   * <code>string airline = 3;</code>
   */
  public java.lang.String getAirline() {
    java.lang.Object ref = airline_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      airline_ = s;
      return s;
    }
  }
  /**
   * <code>string airline = 3;</code>
   */
  public com.google.protobuf.ByteString
      getAirlineBytes() {
    java.lang.Object ref = airline_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      airline_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  public static final int DEPARTUREAIRPORT_FIELD_NUMBER = 4;
  private volatile java.lang.Object departureAirport_;
  /**
   * <code>string departureAirport = 4;</code>
   */
  public java.lang.String getDepartureAirport() {
    java.lang.Object ref = departureAirport_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      departureAirport_ = s;
      return s;
    }
  }
  /**
   * <code>string departureAirport = 4;</code>
   */
  public com.google.protobuf.ByteString
      getDepartureAirportBytes() {
    java.lang.Object ref = departureAirport_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      departureAirport_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  public static final int ARRIVALAIRPORT_FIELD_NUMBER = 5;
  private volatile java.lang.Object arrivalAirport_;
  /**
   * <code>string arrivalAirport = 5;</code>
   */
  public java.lang.String getArrivalAirport() {
    java.lang.Object ref = arrivalAirport_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      arrivalAirport_ = s;
      return s;
    }
  }
  /**
   * <code>string arrivalAirport = 5;</code>
   */
  public com.google.protobuf.ByteString
      getArrivalAirportBytes() {
    java.lang.Object ref = arrivalAirport_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      arrivalAirport_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
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
    if (!getBookingDateBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 1, bookingDate_);
    }
    if (!getFlightDateBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 2, flightDate_);
    }
    if (!getAirlineBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 3, airline_);
    }
    if (!getDepartureAirportBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 4, departureAirport_);
    }
    if (!getArrivalAirportBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 5, arrivalAirport_);
    }
    unknownFields.writeTo(output);
  }

  @java.lang.Override
  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    if (!getBookingDateBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(1, bookingDate_);
    }
    if (!getFlightDateBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(2, flightDate_);
    }
    if (!getAirlineBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(3, airline_);
    }
    if (!getDepartureAirportBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(4, departureAirport_);
    }
    if (!getArrivalAirportBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(5, arrivalAirport_);
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
    if (!(obj instanceof control.proto.SelectedFlight)) {
      return super.equals(obj);
    }
    control.proto.SelectedFlight other = (control.proto.SelectedFlight) obj;

    boolean result = true;
    result = result && getBookingDate()
        .equals(other.getBookingDate());
    result = result && getFlightDate()
        .equals(other.getFlightDate());
    result = result && getAirline()
        .equals(other.getAirline());
    result = result && getDepartureAirport()
        .equals(other.getDepartureAirport());
    result = result && getArrivalAirport()
        .equals(other.getArrivalAirport());
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
    hash = (37 * hash) + BOOKINGDATE_FIELD_NUMBER;
    hash = (53 * hash) + getBookingDate().hashCode();
    hash = (37 * hash) + FLIGHTDATE_FIELD_NUMBER;
    hash = (53 * hash) + getFlightDate().hashCode();
    hash = (37 * hash) + AIRLINE_FIELD_NUMBER;
    hash = (53 * hash) + getAirline().hashCode();
    hash = (37 * hash) + DEPARTUREAIRPORT_FIELD_NUMBER;
    hash = (53 * hash) + getDepartureAirport().hashCode();
    hash = (37 * hash) + ARRIVALAIRPORT_FIELD_NUMBER;
    hash = (53 * hash) + getArrivalAirport().hashCode();
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static control.proto.SelectedFlight parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.SelectedFlight parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.SelectedFlight parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.SelectedFlight parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.SelectedFlight parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static control.proto.SelectedFlight parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static control.proto.SelectedFlight parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static control.proto.SelectedFlight parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static control.proto.SelectedFlight parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static control.proto.SelectedFlight parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static control.proto.SelectedFlight parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static control.proto.SelectedFlight parseFrom(
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
  public static Builder newBuilder(control.proto.SelectedFlight prototype) {
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
   * Protobuf type {@code proto.SelectedFlight}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:proto.SelectedFlight)
      control.proto.SelectedFlightOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return control.proto.Suggestions.internal_static_proto_SelectedFlight_descriptor;
    }

    @java.lang.Override
    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return control.proto.Suggestions.internal_static_proto_SelectedFlight_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              control.proto.SelectedFlight.class, control.proto.SelectedFlight.Builder.class);
    }

    // Construct using control.proto.SelectedFlight.newBuilder()
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
      bookingDate_ = "";

      flightDate_ = "";

      airline_ = "";

      departureAirport_ = "";

      arrivalAirport_ = "";

      return this;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return control.proto.Suggestions.internal_static_proto_SelectedFlight_descriptor;
    }

    @java.lang.Override
    public control.proto.SelectedFlight getDefaultInstanceForType() {
      return control.proto.SelectedFlight.getDefaultInstance();
    }

    @java.lang.Override
    public control.proto.SelectedFlight build() {
      control.proto.SelectedFlight result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    @java.lang.Override
    public control.proto.SelectedFlight buildPartial() {
      control.proto.SelectedFlight result = new control.proto.SelectedFlight(this);
      result.bookingDate_ = bookingDate_;
      result.flightDate_ = flightDate_;
      result.airline_ = airline_;
      result.departureAirport_ = departureAirport_;
      result.arrivalAirport_ = arrivalAirport_;
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
      if (other instanceof control.proto.SelectedFlight) {
        return mergeFrom((control.proto.SelectedFlight)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(control.proto.SelectedFlight other) {
      if (other == control.proto.SelectedFlight.getDefaultInstance()) return this;
      if (!other.getBookingDate().isEmpty()) {
        bookingDate_ = other.bookingDate_;
        onChanged();
      }
      if (!other.getFlightDate().isEmpty()) {
        flightDate_ = other.flightDate_;
        onChanged();
      }
      if (!other.getAirline().isEmpty()) {
        airline_ = other.airline_;
        onChanged();
      }
      if (!other.getDepartureAirport().isEmpty()) {
        departureAirport_ = other.departureAirport_;
        onChanged();
      }
      if (!other.getArrivalAirport().isEmpty()) {
        arrivalAirport_ = other.arrivalAirport_;
        onChanged();
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
      control.proto.SelectedFlight parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (control.proto.SelectedFlight) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }

    private java.lang.Object bookingDate_ = "";
    /**
     * <code>string bookingDate = 1;</code>
     */
    public java.lang.String getBookingDate() {
      java.lang.Object ref = bookingDate_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        bookingDate_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string bookingDate = 1;</code>
     */
    public com.google.protobuf.ByteString
        getBookingDateBytes() {
      java.lang.Object ref = bookingDate_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        bookingDate_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string bookingDate = 1;</code>
     */
    public Builder setBookingDate(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      bookingDate_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string bookingDate = 1;</code>
     */
    public Builder clearBookingDate() {
      
      bookingDate_ = getDefaultInstance().getBookingDate();
      onChanged();
      return this;
    }
    /**
     * <code>string bookingDate = 1;</code>
     */
    public Builder setBookingDateBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      bookingDate_ = value;
      onChanged();
      return this;
    }

    private java.lang.Object flightDate_ = "";
    /**
     * <code>string flightDate = 2;</code>
     */
    public java.lang.String getFlightDate() {
      java.lang.Object ref = flightDate_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        flightDate_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string flightDate = 2;</code>
     */
    public com.google.protobuf.ByteString
        getFlightDateBytes() {
      java.lang.Object ref = flightDate_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        flightDate_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string flightDate = 2;</code>
     */
    public Builder setFlightDate(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      flightDate_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string flightDate = 2;</code>
     */
    public Builder clearFlightDate() {
      
      flightDate_ = getDefaultInstance().getFlightDate();
      onChanged();
      return this;
    }
    /**
     * <code>string flightDate = 2;</code>
     */
    public Builder setFlightDateBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      flightDate_ = value;
      onChanged();
      return this;
    }

    private java.lang.Object airline_ = "";
    /**
     * <code>string airline = 3;</code>
     */
    public java.lang.String getAirline() {
      java.lang.Object ref = airline_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        airline_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string airline = 3;</code>
     */
    public com.google.protobuf.ByteString
        getAirlineBytes() {
      java.lang.Object ref = airline_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        airline_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string airline = 3;</code>
     */
    public Builder setAirline(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      airline_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string airline = 3;</code>
     */
    public Builder clearAirline() {
      
      airline_ = getDefaultInstance().getAirline();
      onChanged();
      return this;
    }
    /**
     * <code>string airline = 3;</code>
     */
    public Builder setAirlineBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      airline_ = value;
      onChanged();
      return this;
    }

    private java.lang.Object departureAirport_ = "";
    /**
     * <code>string departureAirport = 4;</code>
     */
    public java.lang.String getDepartureAirport() {
      java.lang.Object ref = departureAirport_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        departureAirport_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string departureAirport = 4;</code>
     */
    public com.google.protobuf.ByteString
        getDepartureAirportBytes() {
      java.lang.Object ref = departureAirport_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        departureAirport_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string departureAirport = 4;</code>
     */
    public Builder setDepartureAirport(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      departureAirport_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string departureAirport = 4;</code>
     */
    public Builder clearDepartureAirport() {
      
      departureAirport_ = getDefaultInstance().getDepartureAirport();
      onChanged();
      return this;
    }
    /**
     * <code>string departureAirport = 4;</code>
     */
    public Builder setDepartureAirportBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      departureAirport_ = value;
      onChanged();
      return this;
    }

    private java.lang.Object arrivalAirport_ = "";
    /**
     * <code>string arrivalAirport = 5;</code>
     */
    public java.lang.String getArrivalAirport() {
      java.lang.Object ref = arrivalAirport_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        arrivalAirport_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string arrivalAirport = 5;</code>
     */
    public com.google.protobuf.ByteString
        getArrivalAirportBytes() {
      java.lang.Object ref = arrivalAirport_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        arrivalAirport_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string arrivalAirport = 5;</code>
     */
    public Builder setArrivalAirport(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      arrivalAirport_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string arrivalAirport = 5;</code>
     */
    public Builder clearArrivalAirport() {
      
      arrivalAirport_ = getDefaultInstance().getArrivalAirport();
      onChanged();
      return this;
    }
    /**
     * <code>string arrivalAirport = 5;</code>
     */
    public Builder setArrivalAirportBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      arrivalAirport_ = value;
      onChanged();
      return this;
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


    // @@protoc_insertion_point(builder_scope:proto.SelectedFlight)
  }

  // @@protoc_insertion_point(class_scope:proto.SelectedFlight)
  private static final control.proto.SelectedFlight DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new control.proto.SelectedFlight();
  }

  public static control.proto.SelectedFlight getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<SelectedFlight>
      PARSER = new com.google.protobuf.AbstractParser<SelectedFlight>() {
    @java.lang.Override
    public SelectedFlight parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return new SelectedFlight(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<SelectedFlight> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<SelectedFlight> getParserForType() {
    return PARSER;
  }

  @java.lang.Override
  public control.proto.SelectedFlight getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

